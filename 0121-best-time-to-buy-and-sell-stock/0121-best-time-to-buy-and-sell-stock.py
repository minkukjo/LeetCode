class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        num = float('inf')
        result = 0
        for n in prices:
            num = min(num, n)

            if result < n-num:
                result = n-num
        return result