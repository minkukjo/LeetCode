# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def find(node, sub):
        
            if node is None and sub is None:
                return True
            
            if node is None or sub is None:
                return False
            
            return node.val == sub.val and find(node.left, sub.left) and find(node.right, sub.right)
    
        def dfs(node):
            if not node:
                return False

            if find(node, subRoot):
                return True


            return dfs(node.left) or dfs(node.right)

        return dfs(root)
            