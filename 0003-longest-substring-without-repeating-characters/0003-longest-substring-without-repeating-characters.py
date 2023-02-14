class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChgar = {}

        for i in range(len(s)):
            if s[i] in usedChgar and start <= usedChgar[s[i]]:
                start  = usedChgar[s[i]] + 1
            else:
                maxLength=  max(maxLength, i - start + 1)
            usedChgar[s[i]] = i
        return maxLength

