from collections import deque


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = nums[0]
        min1 = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            temp = max1
            max1 = max(nums[i] * max1, nums[i] * min1, nums[i])
            min1 = min(temp*nums[i], nums[i]* min1, nums[i])
            result = max(result, max1)
        return result
