# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import PriorityQueue


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        que = PriorityQueue()
        def dfs(node):
            if node:
                que.put(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)

        ans = 0
        for i in range(k):
            ans = que.get()
        return ans