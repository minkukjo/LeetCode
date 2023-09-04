# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
        
    
    def dfs(self,node):
        if not node: return 0
        
        leftSum = max(0, self.dfs(node.left))
        rightSum = max(0, self.dfs(node.right))
        
        self.max_sum = max(self.max_sum, leftSum + rightSum + node.val)
        return max(leftSum, rightSum) + node.val