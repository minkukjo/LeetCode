class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        def find(node, depth):
            if not node:
                return
            if depth >= len(ans):
                ans.append([])
            ans[depth].append(node.val)
            find(node.left, depth+1)
            find(node.right, depth+1)
        find(root, 0)
        
        return ans

