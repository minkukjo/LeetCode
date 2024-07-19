class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                top_index = stack.pop()
                answer[top_index] = i - top_index

            stack.append(i)

        return answer
