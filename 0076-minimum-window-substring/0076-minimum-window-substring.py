class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ''
        
        t_counter = Counter(t)
        chars = len(t_counter.keys())
        
        s_counter = Counter()
        matches = 0
        
        answer = ''
        
        i = 0
        j = -1 # make j = -1 to start, so we can move it forward and put s[0] in s_counter in the extend phase 
        
        while i < len(s):
            
            # extend
            if matches < chars:
                
                # since we don't have enough matches and j is at the end of the string, we have no way to increase matches
                if j == len(s) - 1:
                    return answer
                
                j += 1
                s_counter[s[j]] += 1
                if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]:
                    matches += 1

            # contract
            else:
                s_counter[s[i]] -= 1
                if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                    matches -= 1
                i += 1
                
            # update answer
            if matches == chars:
                if not answer:
                    answer = s[i:j+1]
                elif (j - i + 1) < len(answer):
                    answer = s[i:j+1]
        
        return answer