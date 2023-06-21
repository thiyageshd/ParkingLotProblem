import unittest
import lib.constants as c
from lib.parking_lot import initialize_models
initialized_dict = initialize_models()

class ParkingLotTests(unittest.TestCase):

    def test_small_parking_area(self):
        ##UseCase1
        vehicle_type = c.MOTORCYCLE
        parking_area = c.SMALL_PARKING_AREA
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ##UseCase2
        vehicle_type = c.MOTORCYCLE
        parking_area = c.SMALL_PARKING_AREA
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 2, parked_vehicle.get('ticket_no') == 2)
        ##UseCase3
        vehicle_type = c.MOTORCYCLE
        parking_area = c.SMALL_PARKING_AREA
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        no_space = parking_details_obj.park()
        self.assertEqual(no_space, c.NO_SPACE)
        ##UseCase4
        vehicle_type = c.MOTORCYCLE
        parking_area = c.SMALL_PARKING_AREA
        ticket_no = 1
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        receipt_details = parking_details_obj.unpark(ticket_no, registration_no="TN39AX4099", \
                                                    minutes=-50)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 2.5)
        ##UseCase5
        vehicle_type = c.MOTORCYCLE
        parking_area = c.SMALL_PARKING_AREA
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 3)
        ###UseCase6
        vehicle_type = c.MOTORCYCLE
        parking_area = c.SMALL_PARKING_AREA
        ticket_no = 3
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        receipt_details = parking_details_obj.unpark(ticket_no, registration_no="TN39AX4101", \
                                                    hours=-22)
        self.assertEquals(receipt_details.get('receipt_no') == "R-2", int(receipt_details.get('fees')) == 110)

    def test_mall_parking_area(self):
        ##UseCase1
        vehicle_type = c.MOTORCYCLE
        parking_area = c.MALL
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ##UseCase2
        vehicle_type = c.LWM
        parking_area = c.MALL
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ##UseCase3
        vehicle_type = c.HWM
        parking_area = c.MALL
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ##UseCase4
        vehicle_type = c.MOTORCYCLE
        parking_area = c.MALL
        ticket_no = 1
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-30, hours=-3)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 40)
        ##UseCase5
        vehicle_type = c.LWM
        parking_area = c.MALL
        ticket_no = 1
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-1, hours=-6)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 140)
        ##UseCase5
        vehicle_type = c.HWM
        parking_area = c.MALL
        ticket_no = 1
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-59, hours=-1)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 100)

    def test_stadium_parking_area(self):
        ##UseCase1
        vehicle_type = c.MOTORCYCLE
        parking_area = c.STADIUM
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ticket_no = 1
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-40, hours=-3)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 30)
        ##UseCase2
        vehicle_type = c.MOTORCYCLE
        parking_area = c.STADIUM
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 2)
        ticket_no = 2
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-59, hours=-14)
        self.assertEquals(receipt_details.get('receipt_no') == "R-2", receipt_details.get('fees') == 390)
        ##UseCase3
        vehicle_type = c.LWM
        parking_area = c.STADIUM
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ticket_no = 1
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-30, hours=-11)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 180)
        ##UseCase4
        vehicle_type = c.LWM
        parking_area = c.STADIUM
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 2)
        ticket_no = 2
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-5, hours=-13)
        self.assertEquals(receipt_details.get('receipt_no') == "R-2", receipt_details.get('fees') == 580)

    def test_airport_parking_area(self):
        ##UseCase1
        vehicle_type = c.MOTORCYCLE
        parking_area = c.AIRPORT
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ticket_no = 1
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-55)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 0)
        ##UseCase2
        vehicle_type = c.MOTORCYCLE
        parking_area = c.AIRPORT
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 2)
        ticket_no = 2
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-59, hours=-14)
        self.assertEquals(receipt_details.get('receipt_no') == "R-2", receipt_details.get('fees') == 60)
        ##UseCase3
        vehicle_type = c.MOTORCYCLE
        parking_area = c.AIRPORT
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 3)
        ticket_no = 3
        receipt_details = parking_details_obj.unpark(ticket_no, hours=-12, days=-1)
        self.assertEquals(receipt_details.get('receipt_no') == "R-3", receipt_details.get('fees') == 160)
        ##UseCase4
        vehicle_type = c.LWM
        parking_area = c.AIRPORT
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 1)
        ticket_no = 1
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-50)
        self.assertEquals(receipt_details.get('receipt_no') == "R-1", receipt_details.get('fees') == 60)
        ##UseCase5
        vehicle_type = c.LWM
        parking_area = c.AIRPORT
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 2)
        ticket_no = 2
        receipt_details = parking_details_obj.unpark(ticket_no, minutes=-59, hours=-23)
        self.assertEquals(receipt_details.get('receipt_no') == "R-2", receipt_details.get('fees') == 80)
        ##UseCase6
        vehicle_type = c.LWM
        parking_area = c.AIRPORT
        parking_details_obj = initialized_dict.get(f"{parking_area}:{vehicle_type}")
        parked_vehicle = parking_details_obj.park()
        self.assertEquals(parked_vehicle.get('spot_no') == 1, parked_vehicle.get('ticket_no') == 3)
        ticket_no = 3
        receipt_details = parking_details_obj.unpark(ticket_no, hours=-1, days=-3)
        self.assertEquals(receipt_details.get('receipt_no') == "R-3", receipt_details.get('fees') == 400)