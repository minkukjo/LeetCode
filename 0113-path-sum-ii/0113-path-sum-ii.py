# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root and root.left is None and root.right is None:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []
        
        ans = []
        def dfs(node, cur, sum):
            if node is None:
                return
            if node.left is None and node.right is None and sum + node.val == targetSum:
                ans.append(cur + [node.val])
            
            
            dfs(node.left, cur + [node.val], sum + node.val)
            dfs(node.right, cur + [node.val], sum + node.val)
        
        dfs(root, [], 0)

        return ans
