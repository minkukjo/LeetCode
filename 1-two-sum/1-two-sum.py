class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            dic[num] = i

        for i, num in enumerate(nums):
            if target - num in dic and i != dic[target - num]:
                return nums.index(num), dic[target-num]