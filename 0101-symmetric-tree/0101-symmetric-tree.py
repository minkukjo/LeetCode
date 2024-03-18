class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(left, right):
            if left == right:
                return True
            if (left is None and right is not None) or (left is not None and right is None) or left.val != right.val:
                return False
            
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)