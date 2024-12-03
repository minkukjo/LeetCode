class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bit = ""
        ans = 0
        while n > 0:
            bit = str(n%2) + bit
            if n%2 == 1:
                ans += 1
            n = n//2

        return ans