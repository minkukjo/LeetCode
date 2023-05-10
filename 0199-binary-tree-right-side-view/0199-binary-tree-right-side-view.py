class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        def dfs(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        dfs(root, 0)
        return view
