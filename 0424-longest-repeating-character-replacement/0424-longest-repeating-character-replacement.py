from typing import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()
        window = 0
        l = 0
        
        for r in range(len(s)):

            c[s[r]] += 1

            if (r - l + 1) - c.most_common()[0][1] > k:
                c[s[l]] -= 1
                l += 1
            
            window = max(window, r-l+1)

        return window

