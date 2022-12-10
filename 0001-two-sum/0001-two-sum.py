class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # hashmap, where key is element and value is index
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return (seen[remainder], i)
            seen[num] = i
        return -1