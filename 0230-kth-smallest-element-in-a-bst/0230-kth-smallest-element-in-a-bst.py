class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        def dfs(node):
            if node is None:
                return

            heappush(heap, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        last = -1
        for i in range(k):
            last = heappop(heap)

        return last