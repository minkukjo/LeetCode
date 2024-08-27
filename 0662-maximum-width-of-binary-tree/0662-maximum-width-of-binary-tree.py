# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        layer = defaultdict(list)


        def dfs(node, depth, index):
            if node is None:
                return
            
            layer[depth].append(index)
            
            
            
            dfs(node.left, depth+1, 2*index + 1)
            dfs(node.right, depth+1,  2*index + 2)
        dfs(root, 0, 0)

        max_len = 0
        
        for _ ,v in layer.items():
            max_len = max(max_len, max(v) - min(v)+1)
            
        return max_len