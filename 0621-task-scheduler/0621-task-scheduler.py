from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        max_frequent = max(count.values())
        freq = list(count.values())
        last_row = freq.count(max_frequent)
        return max((max_frequent -1) * ( n+1) + last_row,len(tasks))