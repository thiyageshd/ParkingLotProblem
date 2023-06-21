from cache.lfucache import LFUCollector

class SpecCollector(LFUCollector):
    def __init__(self, max_size):
        LFUCollector.__init__(self, max_size)