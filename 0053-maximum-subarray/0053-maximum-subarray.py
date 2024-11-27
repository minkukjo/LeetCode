class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        cur = float("-inf")

        for num in nums:
            cur = max(num, cur+num)
            answer = max(answer, cur)
        return answer