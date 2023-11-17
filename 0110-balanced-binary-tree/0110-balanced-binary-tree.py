# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def findDepth(node):

            if node is None:
                return 0
            
            left_depth = findDepth(node.left)
            righgt_depth = findDepth(node.right)
            if left_depth == -1 or righgt_depth == -1 or abs(left_depth - righgt_depth) > 1:
                return -1
            return 1 + max(left_depth,righgt_depth)

        return findDepth(root) != -1

