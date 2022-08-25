class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for c in nums:
            if(curSum <0):
                curSum = 0
            curSum += c
            maxSub = max(maxSub, curSum)
        return maxSub
