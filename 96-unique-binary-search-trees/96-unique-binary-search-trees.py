class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * 20
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            total = 0
            for j in range(0, i):
                left = dp[j]
                right = dp[i-j-1]
                total += left * right
            dp[i] = total
        return dp[n]
