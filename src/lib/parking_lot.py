

from lib.models import ParkingDetails, EmployeeVehicleDetails
from lib.config import fee_config, employee_vehicle_data
import cache.spec_store as spec_store

def initialize_models():
    '''
    Initialize the class object for all the types of Parking areas and Vehicles available
    This is to make sure we have the LFU cache ready for each Parking Area
    In Case of DB, we might not need this initialization
    '''
    employee_parking_store = allocate_parking_to_employee()
    initialized_dict = {}
    for parking_area, vechicle_dict in fee_config.items():
        for vehicle_type in vechicle_dict:
            if vehicle_type in ["hourly_rate", "summing_up"]:
                continue
            parking_details_obj = ParkingDetails(parking_area, vehicle_type, employee_parking_store)
            parking_details_obj.initialize_vechile_prop(parking_area, vehicle_type)
            initialized_dict[f"{parking_area}:{vehicle_type}"] = parking_details_obj
    return initialized_dict


def allocate_parking_to_employee():
    '''
    This registers the employee data once when initialized
    '''
    spec_collector = spec_store.SpecCollector(100)
    for data in employee_vehicle_data:
        employee_name, registration_no, sticker = data
        emp_obj = EmployeeVehicleDetails(employee_name, registration_no, sticker)
        spec_collector.register_employee_details(emp_obj, registration_no)
    return spec_collector

if __name__ == '__main__':
    pass