class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        dic = {}

        q = []
        q.append((root,0))

        while q:
            (node, level) = q.pop(0)
            if level not in dic:
                dic[level] = [node.val]
            else:
                dic[level].append(node.val)

            if node.left is not None:
                q.append((node.left,level+1))

            if node.right is not None:
                q.append((node.right,level+1))
        for key, value in dic.items():
            result.append(value)
        return result