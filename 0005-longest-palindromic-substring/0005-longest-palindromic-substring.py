class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def find(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        def longest(a, b, c):
            len1 = len(a)
            len2 = len(b)
            len3 = len(c)

            if len1 >= len2 and len1 >= len3:
                return a
            elif len2 >= len1 and len2 >= len3:
                return b
            else:
                return c

        ans = ""
        for i in range(len(s)):
            one = find(i,i)
            two = find(i,i+1)

            ans = longest(ans,one,two)
            
        return ans