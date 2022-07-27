class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 1:
            return 0

        maxLeft = []
        maxRight = []

        maxLeftValue = 0
        for i in range(len(height)):
            maxLeft.append(maxLeftValue)
            maxLeftValue = max(maxLeftValue, height[i])

        maxRightValue = 0
        for i, value in reversed(list(enumerate(height))):
            maxRight.append(maxRightValue)
            maxRightValue = max(maxRightValue, height[i])

        maxRight.reverse()
         
        results = []
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            water = water if water >= 0 else 0
            results.append(water)
        
        return sum(results)