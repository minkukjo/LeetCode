from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        distance = set(nums)

        for i, num in enumerate(nums):
            if target - num in distance:
                target_index = nums.index(target-num)
                if i != target_index:
                    return [i, target_index]
        