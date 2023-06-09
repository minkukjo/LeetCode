class Solution:
    def climbStairs(self, n: int) -> int:
        str = [0,1,2] + [-1] * (n-2)

        def dp(str, i):
            if str[i] == -1:
                str[i] = dp(str, i-1) + dp(str, i-2)
            return str[i]
        return dp(str, n)

        