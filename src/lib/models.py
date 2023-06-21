import lib.constants as c
import lib.utils as utils
import cache.spec_store as spec_store
from datetime import datetime, timedelta
from lib.config import fee_config, discount_config


class EmployeeVehicleDetails():
    def __init__(self, employee_name, vehicle_reg_no, sticker_type):
        self.employee_name = employee_name
        self.vehicle_reg_no = vehicle_reg_no
        self.sticker_type = sticker_type

class ParkedVehicle():
    __slots__ = ('spot_no', 'ticket_no', 'entry_time', 'receipt_no', 'exit_time', 'fees')
    _allowed = ('receipt_no', 'exit_time', 'fees')
    def __init__(self, spot_no, ticket_no, entry_time, **kwargs):
        self.spot_no = spot_no
        self.ticket_no = ticket_no
        self.entry_time = entry_time
        for k, v in kwargs.items():
            assert( k in self.__class__._allowed)
            setattr(self, k, v)

class ParkingSlot():
    def __init__(self, parking_area):
        self.parking_area = parking_area
        ###TODO - Everytime when the program restarts, this count will be reinitialized. To Avoid we need to use DB
        self.ticket_count = utils.count()
        self.receipt_count = utils.count()

class Vehicle(ParkingSlot):
    def __init__(self, parking_area, vehicle_type):
        self.vehicle_type = vehicle_type
        ParkingSlot.__init__(self, parking_area)

class ParkingDetails(Vehicle):
    def __init__(self, parking_area, vehicle_type, employee_parking_store):
        self.fee_structure = fee_config.get(parking_area)
        self.hourly_rate = self.fee_structure.get("hourly_rate", False)
        self.spots = self.fee_structure.get(vehicle_type, {}).get("spots")
        self.employee_parking_store = employee_parking_store
        self.per_day_charge = False
        if parking_area == c.AIRPORT:
            self.per_day_charge = True
        self.invalid_vehicle = False
        if not self.spots:
            self.invalid_vehicle = True
            self.spec_collector = None
        else:
            self.spec_collector = spec_store.SpecCollector(self.spots)

    def initialize_vechile_prop(self, parking_area, vehicle_type):
        ###TODO Initialize once while defining the config.
        Vehicle.__init__(self, parking_area, vehicle_type)

    def park(self):
        if self.invalid_vehicle:
            return c.INVALID_VEHICLE_PARK
        self.parked_vehicle_list = self.spec_collector.parsed_value(self.parking_area, self.vehicle_type)
        if self.parked_vehicle_list and len(self.parked_vehicle_list) >= self.spots:
            return c.NO_SPACE
        self.spot_no = self.get_next_free_spot()
        if self.spot_no is None:
            return c.ISSUE_WITH_SPOT_ALLOCATION
        self.ticket_number = next(self.ticket_count)
        self.entry_time = datetime.now()
        parked_vehicle = {
                        "spot_no": self.spot_no,
                        "ticket_no": self.ticket_number,
                        "entry_time": self.entry_time
                    }
        parked_vehicle_obj = ParkedVehicle(self.spot_no, self.ticket_number, self.entry_time)
        self.parked_vehicle_list.append(parked_vehicle_obj)
        self.spec_collector.register_value(self.parking_area, self.vehicle_type, self.parked_vehicle_list, hashed_value=None)
        return parked_vehicle

    def unpark(self, ticket_no, registration_no=None, **kwargs):
        if self.invalid_vehicle:
            return c.INVALID_VEHICLE_UNPARK
        self.parked_vehicle_list = self.spec_collector.parsed_value(self.parking_area, self.vehicle_type)
        stored_key_index = [i for i in range(len(self.parked_vehicle_list)) if self.parked_vehicle_list[i].ticket_no == ticket_no]
        stored_key_index = stored_key_index[0] if stored_key_index else None
        if stored_key_index is None:
            return f"Vehicle with ticket_no - {ticket_no} is not parked in this area."
        removed_val = self.parked_vehicle_list[stored_key_index]
        self.parked_vehicle_list = self.spec_collector.remove_value(stored_key_index, self.parking_area, self.vehicle_type)
        receipt_no = f"R-{next(self.receipt_count)}"
        exit_time = datetime.now() - timedelta(hours=kwargs.get("hours", 0), minutes=kwargs.get("minutes", 0), days=kwargs.get("days", 0))
        entry_time = removed_val.entry_time
        return {
            "receipt_no": receipt_no,
            "entry_time": entry_time,
            "exit_time": exit_time,
            "fees": self.calculate_fees(entry_time, exit_time, registration_no)
        }

    def get_next_free_spot(self):
        stored_spots = [i.spot_no for i in self.parked_vehicle_list]
        total_spots = list(range(1, self.spots+1))
        available_spots = list(set(total_spots) - set(stored_spots))
        available_spots.sort()
        return available_spots[0] if available_spots else None

    def calculate_fees(self, entry_time, exit_time, registration_no):
        usage = exit_time-entry_time
        days = usage.days
        seconds = usage.seconds
        hours =  self.get_hour(seconds)
        fee_dict = self.fee_structure.get(self.vehicle_type)
        summing_up = self.fee_structure.get("summing_up", False)
        if not self.hourly_rate:
            hourly_fees = fee_dict.get("fee")
            if days:
                hours += days*24
            total_fee = hours*hourly_fees
            return self.calculate_discounted_fee(total_fee, registration_no)
        total_fee = self.get_total_fee(hours, days, fee_dict, summing_up)
        return self.calculate_discounted_fee(total_fee, registration_no)

    def calculate_discounted_fee(self, total_fee, registration_no):
        if not registration_no:
            return total_fee
        emp_obj = self.employee_parking_store.fetch_register_value(registration_no)
        sticket_type = emp_obj.sticker_type
        discount = discount_config.get(sticket_type, 0)
        return total_fee * ((100-discount)/100) if discount else total_fee

    def get_total_fee(self, hours, days, fee_dict, summing_up):
        hourly_dict = fee_dict.get("fee")
        day_charge = fee_dict.get("day")
        total_fee = 0
        for k, fee in hourly_dict.items():
            from_h, to_h = int(k.split('-')[0]), int(k.split('-')[-1])
            if self.per_day_charge and days>0:
                days += 1 if hours else 0
                return day_charge*days
            if from_h == to_h and not self.per_day_charge:
                hourly_fee = hourly_dict.get(str(from_h))
                hours += days*24
                total_fee += (hours-from_h)*hourly_fee
                return total_fee
            elif hours >= from_h and hours <= to_h:
                if summing_up:
                    total_fee +=  fee
                else:
                    total_fee = fee
                break
            else:
                if summing_up:
                    total_fee += fee

        return total_fee

    def get_hour(self, seconds):
        h = seconds/(60*60)
        if float(h) == int(h):
            return h
        return int(h)+1