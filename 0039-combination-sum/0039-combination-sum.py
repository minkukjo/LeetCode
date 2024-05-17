class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def dfs(list, cur, index):

            if cur == target:
                result.append(list)
                return
            if cur > target:
                return

            for i in range(index, len(candidates)):
                dfs(list + [candidates[i]], cur+candidates[i], i)
        dfs([], 0, 0)
        return result