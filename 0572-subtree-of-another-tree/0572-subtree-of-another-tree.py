class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return False

            if isSame(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        def isSame(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 and node2 and node1.val == node2.val:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
            return False
        
        return dfs(root)