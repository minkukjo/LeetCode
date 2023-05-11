class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        ans = [0]
        
        def dfs(node, cur):
            if node:

                if node.val >= cur:
                    ans[0] += 1
                    cur = node.val
                dfs(node.left, cur)
                dfs(node.right, cur)
        dfs(root, root.val)
        return ans[0]
