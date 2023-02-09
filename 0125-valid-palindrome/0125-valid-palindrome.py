class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                str += c.lower()

        print(str)
        return str == str[::-1]