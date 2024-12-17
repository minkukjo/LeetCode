class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(sum):
            if sum > target:
                return 0
            if target -sum == 0:
                return 1
            if sum in memo:
                return memo[sum]
            ans = 0
            for num in nums:
                ans = ans + dfs(sum + num)
            memo[sum] = ans
            return ans
       
        return dfs(0)