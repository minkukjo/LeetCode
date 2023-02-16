class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        count = defaultdict(int)
        length = 0
        answer = 0
        while r < len(s):
            count[s[r]] += 1

            length = max(length, count[s[r]]) 

            if ((r-l+1) - length <= k):
                answer = max(answer , r-l+1)
            else:
                count[s[l]] -= 1
                l += 1
            r += 1
        return answer