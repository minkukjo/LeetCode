class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        for i in nums:
            once ^= i
        return once