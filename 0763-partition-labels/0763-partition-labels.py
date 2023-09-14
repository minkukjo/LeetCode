class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hash = {}

        for i in range(len(s)):

            hash[s[i]] = i

        size = 0
        end = 0
        ans = []
        for i  in range(len(s)):
            size += 1
            end = max(end, hash[s[i]])


            if i == end:
                ans.append(size)
                size = 0
                end = 0
        return ans