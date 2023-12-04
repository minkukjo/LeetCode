from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)

        if len(c) == 1:
            return len(s)

        result = 0
        odd = 0
        for e in c.values():
            if e % 2 == 0:
                result += e
            else:
                odd = 1
                result += (e-1)
        return result + odd