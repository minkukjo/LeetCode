class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end( key )
            return self.cache[key]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len( self.cache ) >= self.capacity :
                # pop the least used entry
                self.cache.popitem( last = False )

        else:
			# refresh the entry with given key
            self.cache.move_to_end( key )
        
        self.cache[ key ] = value