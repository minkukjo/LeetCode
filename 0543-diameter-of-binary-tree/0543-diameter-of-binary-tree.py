# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0
        
        self.depth(root)

        return self.diameter
    
    def depth(self, node):
        if not node:
            return 0
            
        left = self.depth(node.left)
        right = self.depth(node.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)