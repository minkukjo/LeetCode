class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        
        self.dfs(ans,0,[],nums)
        return ans
    def dfs(self, ans, start, sub, nums):
        ans.append(list(sub))
        for i in range(start, len(nums)):
            sub.append(nums[i])
            self.dfs(ans, i+1, sub, nums)
            sub.pop()


