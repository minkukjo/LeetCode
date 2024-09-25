class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(depth,root, direction):
            if root is None:
                return
            if len(ans)<=depth:
                ans.append([])
            if direction:
                ans[depth].append(root.val)
            else:
                ans[depth].insert(0,root.val)
            dfs(depth+1,root.left,not direction)
            dfs(depth+1,root.right,not direction)    
        dfs(0,root, True)
        return ans