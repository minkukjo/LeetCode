class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = {}
        result = 0
        left = 0
        for right, char in enumerate(s):
            if char in checker and left <= checker[char]:
                left = checker[char] + 1
            else:
                result = max(result, right - left + 1)
            checker[char] = right
        return result
