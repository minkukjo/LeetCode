from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        checker = set()
        stack = []
        for char in s:
            counter[char] -= 1

            if char in checker:
                continue

            while stack and char <= stack[-1] and counter[stack[-1]] > 0:
                checker.remove(stack.pop())
            stack.append(char)
            checker.add(char)

        return ''.join(s for s in stack)