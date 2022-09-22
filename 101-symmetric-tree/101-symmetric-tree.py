class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right

        if root and left is None and right is None:
            return True
        if root and left and right and left.val != right.val:
            return False
        if root is None or left is None or right is None:
            return False

        def dfs(left, right):
            if left is None and right is None:
                return True
            if (left is None and right) or (right is None and left) or left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(left.left, right.right) and dfs(left.right, right.left)