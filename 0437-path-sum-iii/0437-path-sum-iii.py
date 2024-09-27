# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ans = [0]

        def find(node, target):
            if not node:
                return
            if node.val == target:
                ans[0] += 1
            find(node.left, target - node.val)
            find(node.right, target - node.val)


        def dfs(node, target):
            if not node:
                return 0
            find(node, target)
            left = dfs(node.left, target)
            right = dfs(node.right, target)
        dfs(root, targetSum)
        return ans[0]
