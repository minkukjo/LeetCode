from queue import PriorityQueue
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()

        for num in nums:
            q.put(-num)
        
        ans = 0
        for i in range(k):
            ans = -q.get()
        return ans