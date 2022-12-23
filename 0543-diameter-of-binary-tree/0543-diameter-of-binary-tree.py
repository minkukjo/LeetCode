class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.dfs(root)

        return self.diameter

    def dfs(self,root):
        if not root:
            return 0 

        leftCount = self.dfs(root.left)
        rightCount = self.dfs(root.right)

        self.diameter = max(self.diameter, leftCount + rightCount)

        return max(leftCount, rightCount) + 1