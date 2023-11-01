from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_len = 0
        used_char = {}
        
        for i in range(len(s)):
            
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            used_char[s[i]] = i
        return max_len