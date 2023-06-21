import random, string
from datetime import datetime, timedelta
from geopy import distance

class RandomGenerator():
    def latitude_generator(self):
        return random.uniform(50,60)

    def longitude_generator(self):
        return random.uniform(15,22)

    def price_generator(self):
        return random.randint(5,10)

    def name_generator(self):
        return ''.join(random.choices(string.ascii_letters, k=10))

    def address_generator(self):
        return ''.join(random.choices(string.ascii_letters, k=25))

    def pickup_time(self):
        return datetime.now() + timedelta(minutes=random.randint(1,60))

def distance_bet_two_points(coords_1, coords_2):
    return distance.geodesic(coords_1, coords_2)