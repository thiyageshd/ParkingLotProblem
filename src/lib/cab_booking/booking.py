from lib.cab_booking.spec_store import SpecCollector
import random
import lib.cab_booking.utils as utils
from lib.cab_booking.config import Driver, RideDetails, BookingStatus

driver_store = SpecCollector(100)
ride_store = SpecCollector(100)
booking_store = SpecCollector(1000)

def generate_driver_details():
    for i in range(100):
        driver_obj = Driver()
        key = f"{driver_obj.latitude_loc}:{driver_obj.longitude_loc}"
        driver_store.register_value(key, driver_obj.__dict__)

def generate_ride_details():
    for i in range(100):
        ride_obj = RideDetails()
        key = f"{ride_obj.pick_latitude}:{ride_obj.pick_logitude}"
        ride_store.register_value(key, ride_obj.__dict__)

def get_efficient_driver(ride_details):
    driver_details = get_nearest_driver(ride_details)
    return driver_details

def get_nearest_driver(ride_details):
    nearest_driver = {}
    for loc, driver_details in driver_store.learning_dict._Cache__data.items():
        if booking_store.parsed_value(driver_details['id']):
            continue
        dri_lat, dri_long = loc.split(':')
        g_obj = utils.distance_bet_two_points((dri_lat, dri_long), (ride_details['pick_latitude'], ride_details['pick_logitude']))
        nearest_driver[g_obj.km] = {
            'loc': loc,
            'charges': g_obj.km * driver_details['price_per_km'],
            'id': driver_details['id'],
            'name': driver_details['name'],
            'address': driver_details['address']
        }
    nearest_driver = get_sorted_dict(nearest_driver)
    minimum_charges=dict(sorted(nearest_driver.items(),key= lambda x:x[1]['charges']))
    driver_details = minimum_charges[list(minimum_charges.keys())[0]]
    return driver_details

def update_driver_location(driver_loc, drop_latitude, drop_logitude):
    stored_data = driver_store.parsed_value(driver_loc)
    driver_store.remove_value(driver_loc)
    stored_data['latitude_loc'] = drop_latitude
    stored_data['longitude_loc'] = drop_logitude
    key = f"{drop_latitude}:{drop_logitude}"
    driver_store.register_value(key, stored_data)

def get_sorted_dict(nearest_driver):
    d = {}
    for k in sorted(nearest_driver):
        d[k] = nearest_driver[k]
    return d

if __name__ == '__main__':
    generate_driver_details()
    generate_ride_details()
    # for i in range(5):
    #     ride_keys = list(ride_store.learning_dict._Cache__data.keys())
    #     ride_key = ride_keys[random.randint(1,100)]
    #     ride_details = ride_store.learning_dict._Cache__data[ride_key]
    #     driver_details = get_efficient_driver(ride_details)
    #     booking_obj = BookingStatus(driver_details['id'], driver_details['name'],
    #                   ride_details['drop_latitude'], ride_details['drop_logitude'])
    #     booking_store.register_value(driver_details['id'], booking_obj)
    #     update_driver_location(driver_details, ride_details)