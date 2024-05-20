class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        def dfs(cur):

            if len(cur) == n:
                ans.append(cur)
                return
            
            for num in nums:
                if num not in cur:
                    dfs(cur + [num])

        for num in nums:
            dfs([num])

        return ans