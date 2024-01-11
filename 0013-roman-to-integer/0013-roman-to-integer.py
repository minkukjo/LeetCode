class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        value = 0
        for i in range(len(s)):
            if i <len(s) -1 and m[s[i]] < m[s[i+1]]:
                value -= m[s[i]]
            else:
                value += m[s[i]]
                

        return value