class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_l = [0] * len(height)
        max_r = [0] * len(height)

        l = 0

        for i in range(len(height)):
            max_l[i] = l
            l = max(height[i], l)

        r = 0
        for i in range(len(height)-1, -1,-1):
            max_r[i] = r
            r = max(height[i], r)
        
        ans = []
        for i in range(len(height)):
            water = min(max_l[i], max_r[i]) - height[i]
            if water < 0:
                ans.append(0)
            else:
                ans.append(water)
        return sum(ans)

