import lib.cab_booking.utils as utils
from uuid import uuid4

class Person():
    def __init__(self, name, address) :
        self.name = name
        self.address = address

class Driver(Person):
    def __init__(self):
        self.random_obj = utils.RandomGenerator()
        self.id = str(uuid4())
        Person.__init__(self, self.random_obj.name_generator(), self.random_obj.address_generator())
        self.latitude_loc = self.random_obj.latitude_generator()
        self.longitude_loc = self.random_obj.longitude_generator()
        self.price_per_km = self.random_obj.price_generator() #### Price are in USD

class BookingStatus():
    def __init__(self, loc, d_id, name, latitude_drop, longitude_drop):
        self.loc = loc
        self.driver_id = d_id
        self.driver_name = name
        self.latitude_drop = latitude_drop
        self.longitude_drop = longitude_drop

class RideDetails():
    def __init__(self) -> None:
        self.random_obj = utils.RandomGenerator()
        self.id = str(uuid4())
        self.pickup_time = self.random_obj.pickup_time()
        self.pick_latitude = self.random_obj.latitude_generator()
        self.pick_logitude = self.random_obj.longitude_generator()
        self.pick_address = self.random_obj.address_generator()
        self.drop_latitude = self.random_obj.latitude_generator()
        self.drop_logitude = self.random_obj.longitude_generator()