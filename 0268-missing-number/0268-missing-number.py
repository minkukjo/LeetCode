class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for num in nums:
            missing ^= num
        for i in range(len(nums) + 1):
            missing ^= i
        return missing
