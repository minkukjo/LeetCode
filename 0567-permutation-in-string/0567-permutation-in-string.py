from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)

        for i in range(len(s2)-len(s1)+1):
            if s1_counter == Counter(s2[i:i+len(s1)]):
                return True
        return False