class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1

        def dfs(node, sum):
            if not node:
                return
            
            sum += node.val
            self.total += self.lookup[sum]
            self.lookup[targetSum+sum] += 1
            dfs(node.left, sum)
            dfs(node.right, sum)
            self.lookup[targetSum+sum] -= 1
        
        dfs(root,0)
        return self.total
            