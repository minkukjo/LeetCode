
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        answer = nums[0]
        cur = float("-inf")
        for num in nums:
            cur = max(cur + num, num)
            answer = max(answer, cur)
        return answer




        