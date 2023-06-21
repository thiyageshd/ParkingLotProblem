from enum import Enum
from cachetools import LFUCache
import jsonpickle

class ValueFoundIn(Enum):
    IN_MEMORY = 0
    AFTER_REGISTRATION = 1

class LFUCollector():
    def __init__(self, maxsize):
        self.learning_dict = LFUCache(maxsize=maxsize)
        self.found_in = ValueFoundIn.AFTER_REGISTRATION

    def make_hashed_value(self, cache_key) -> str:
        value = jsonpickle.encode({'cache_key': cache_key})
        return make_hash_from_value(value)

    def register_value(self, cache_key, value, hashed_value=None):
        # if hashed_value is None:
        #     hashed_value = self.make_hashed_value(cache_key)
        self.learning_dict[cache_key] = value

    def parsed_value(self, cache_key):
        # hashed_value = self.make_hashed_value(cache_key)
        stored_value = self.learning_dict.get(cache_key)
        if stored_value is None:
            return []
        self.found_in = ValueFoundIn.IN_MEMORY
        return stored_value

    def remove_value(self, cache_key):
        # hashed_value = self.make_hashed_value(cache_key)
        stored_value = self.learning_dict.get(cache_key)
        if stored_value:
            self.learning_dict.pop(cache_key)
        return stored_value

def make_hash_from_value(data):
    import hashlib
    md5_object = hashlib.sha512()
    md5_object.update(data.encode('utf-8'))
    md5_hash = md5_object.hexdigest()
    return md5_hash