class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) -1

        ans = 0
        while l<r:

            w = r-l
            s = min(height[l],height[r])

            ans = max(ans, w*s)

            if height[l] < height[r] :
                l += 1
            else:
                r -= 1
        return ans