from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(magazine)
        
        for c in ransomNote:
            if c in r and r[c] > 0:
                r[c] -= 1
            else:
                return False
        return True