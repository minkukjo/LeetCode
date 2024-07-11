from collections import OrderedDict, defaultdict, deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

        

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        
        if len(self.cache.keys()) > self.capacity:
            # last=False means FIFO
            # If last is True, it's gonig to be LILO
            return self.cache.popitem(last=False)

        