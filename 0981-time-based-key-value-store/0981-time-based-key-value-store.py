class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        if not values: return ''
        left, right = 0, len(values)-1
        while left < right:
            mid = (left+ right + 1) // 2
            pre_timestamp, _ = values[mid]
            if pre_timestamp > timestamp:
                right= mid-1
            else:
                left= mid
        
        return values[left][1] if values[left][0] <= timestamp else ''