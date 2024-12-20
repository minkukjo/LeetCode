class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)

        if len(nums) <= 3:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]

        for i in range(3, len(nums)-1):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])



        nums2 = nums[1:]
        dp2 = [0] * len(nums2)
        dp2[0] = nums2[0]
        dp2[1] = nums2[1]
        dp2[2] = nums2[0] + nums2[2]

        for i in range(3, len(nums2)):
            dp2[i] = nums2[i] + max(dp2[i-2],dp2[i-3])
        
        return max(max(dp), max(dp2))