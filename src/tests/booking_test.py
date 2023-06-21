import unittest
import random
import lib.constants as c
from lib.cab_booking.config import BookingStatus
from lib.cab_booking.booking import generate_driver_details, generate_ride_details
import lib.cab_booking.booking as b

class CabBooking(unittest.TestCase):
    setup_done = False
    def setUp(self):
        if CabBooking.setup_done:
            return
        generate_driver_details()
        generate_ride_details()
        CabBooking.setup_done = True

    def test_booking(self):
        ride_keys = list(b.ride_store.learning_dict._Cache__data.keys())
        for i in range(5):
            ride_key = ride_keys[random.randint(1,100)]
            ride_details = b.ride_store.learning_dict._Cache__data[ride_key]
            driver_details = b.get_efficient_driver(ride_details)
            booking_obj = BookingStatus(driver_details['loc'], driver_details['id'], driver_details['name'],
                        ride_details['drop_latitude'], ride_details['drop_logitude'])
            b.booking_store.register_value(driver_details['id'], booking_obj)

    def test_close_booking(self):
        driver_ids = b.booking_store.learning_dict._Cache__data.keys()
        for id in driver_ids:
            removed_value = b.booking_store.remove_value(id)
            b.update_driver_location(removed_value.loc, \
                                        removed_value.latitude_drop, \
                                        removed_value.longitude_drop)