from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = len(temperatures) * [0]
        for i, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                left = stack.pop()
                answer[left] = i - left
            stack.append(i)
        return answer