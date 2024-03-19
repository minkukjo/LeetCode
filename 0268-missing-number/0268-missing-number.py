class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        nums.sort()

        start = 0
        for i in range(n):
            if start != nums[i]:
                return start
            start +=1
        return n
