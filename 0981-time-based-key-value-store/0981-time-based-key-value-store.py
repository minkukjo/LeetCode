from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.s = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append([value , timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.s.get(key,[])
        l,r = 0, len(values)-1

        ans = ""
        while l<=r:
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                l = mid+1
                ans = values[mid][0]
            else:
                r = mid -1
        return ans

