from enum import Enum
import typing
from cachetools import LFUCache
import jsonpickle

class ValueFoundIn(Enum):
    IN_MEMORY = 0
    AFTER_REGISTRATION = 1

class LFUCollector():
    def __init__(self, maxsize):
        self.learning_dict = LFUCache(maxsize=maxsize)
        self.found_in = ValueFoundIn.AFTER_REGISTRATION

    def make_hashed_value(self, parking_area, vehicle_type) -> str:
        value = jsonpickle.encode({'parking_area': parking_area, 'vehicle_type': vehicle_type})
        return make_hash_from_value(value)

    def register_value(self, parking_area, vehicle_type, value, hashed_value: typing.Optional[str]):
        if hashed_value is None:
            hashed_value = self.make_hashed_value(parking_area, vehicle_type)
        self.learning_dict[hashed_value] = value

    def register_employee_details(self, value, registration_no):
        hashed_value = make_hash_from_value(registration_no)
        self.learning_dict[hashed_value] = value

    def fetch_register_value(self, registration_no):
        hashed_value = make_hash_from_value(registration_no)
        stored_value = self.learning_dict.get(hashed_value)
        if stored_value is None:
            return None
        return stored_value

    def parsed_value(self, parking_area, vehicle_type):
        hashed_value = self.make_hashed_value(parking_area, vehicle_type)
        stored_value = self.learning_dict.get(hashed_value)
        if stored_value is None:
            return []
        self.found_in = ValueFoundIn.IN_MEMORY
        return stored_value

    def remove_value(self, stored_key_index, parking_area, vehicle_type):
        hashed_value = self.make_hashed_value(parking_area, vehicle_type)
        stored_value = self.learning_dict.get(hashed_value)
        if stored_value and stored_value[stored_key_index]:
            stored_value.pop(stored_key_index)
            self.learning_dict[hashed_value] = stored_value
            return stored_value
        return stored_value

def make_hash_from_value(data):
    import hashlib
    md5_object = hashlib.sha512()
    md5_object.update(data.encode('utf-8'))
    md5_hash = md5_object.hexdigest()
    return md5_hash