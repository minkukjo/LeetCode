from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def dfs(cur, cur_len):
            if cur_len == len(nums):
                if cur not in ans:
                    ans.append(cur)
                return
            
            for num in nums:
                if num not in cur:
                    dfs(cur + [num], cur_len+1)

        for num in nums:
            dfs([num], 1)
        return ans

s = Solution()
s.permute([1,2,3])