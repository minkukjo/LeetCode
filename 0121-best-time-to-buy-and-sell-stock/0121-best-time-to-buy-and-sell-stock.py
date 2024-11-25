class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        most_low = prices[0]
        answer = 0

        for price in prices:
            if price - most_low > answer:
                answer = price - most_low

            most_low = min(most_low, price)
        return answer
