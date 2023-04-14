class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        result = []

        def dfs(arr: List[int], index, candidates, target):
            if index >= len(candidates):
                return
            if sum(arr) > target:
                return
            if sum(arr) == target:
                result.append(arr.copy())
                return
                
            if sum(arr) < target:
                arr.append(candidates[index])
                dfs(arr, index, candidates, target)
                arr.pop()
                dfs(arr, index+1, candidates, target)
        dfs([],0,candidates,target)
        return result
    