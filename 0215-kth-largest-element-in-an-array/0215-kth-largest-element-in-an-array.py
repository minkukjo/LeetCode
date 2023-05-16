class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        result = -1
        while k > 0:
            k -= 1
            result = heapq._heappop_max(nums)
        return result

        