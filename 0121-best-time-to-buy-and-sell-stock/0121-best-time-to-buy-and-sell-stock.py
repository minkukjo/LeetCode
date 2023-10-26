class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_value = prices[0]
        result = 0

        for i in range(1, len(prices)):
            result = max(result, prices[i] - min_value)
            min_value = min(min_value, prices[i])
        return result