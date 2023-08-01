class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(low, high):
            while low>=0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1
            return s[low+1: high]

        res = ''
        for i in range(len(s)):
            s1 = isPalindrome(i,i)
            s2 = isPalindrome(i,i+1)

            if len(s1) > len(res):
                res = s1
                
            if len(s2) > len(res):
                res = s2
        return res