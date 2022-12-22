class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = Counter(p)
        pl = len(p)
        answer = []

        for i, l in enumerate(s):
            
            if len(s) - pl < i:
                break

            if Counter(s[i:i+pl]) == c:
                answer.append(i)
        return answer