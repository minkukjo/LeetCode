
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCounter = Counter(p)
        sCounter = Counter(s[0:len(p)])
        answer = [0] if pCounter == sCounter else []

        l = 0
        for r in range(len(p),len(s)):
            sCounter[s[r]] = 1 + sCounter.get(s[r],0)
            sCounter[s[l]] -= 1


            if sCounter[s[l]] == 0:
                sCounter.pop(s[l])
            l += 1
            if sCounter == pCounter:
                answer.append(l)
            
            
        return answer