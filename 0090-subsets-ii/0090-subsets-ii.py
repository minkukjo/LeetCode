class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                if curr not in res: res.append(curr[:])
                return

            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)

        dfs(0)
        return res