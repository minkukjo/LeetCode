class Solution:
    def depth(self, node: Optional[TreeNode]) -> int:
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0

        if left + right > self.diameter:
            self.diameter = left + right
        print("left:",str(left))
        print("right:",str(right))
        return 1 + (left if left > right else right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter