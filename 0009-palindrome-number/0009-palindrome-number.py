class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        t = str(x)

        return t == t[::-1]