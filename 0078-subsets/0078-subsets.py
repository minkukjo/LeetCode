class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(arr, i):
            if i == len(nums):
                ans.append(list(arr))
                return
            
            arr.append(nums[i])
            dfs(arr, i+1)
            arr.pop()
            dfs(arr,i+1)

        dfs([],0)
        return ans