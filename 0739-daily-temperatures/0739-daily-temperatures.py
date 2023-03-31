class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for t in range(len(temperatures))]
        for i, value in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < value:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        return ans