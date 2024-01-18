# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p == None and q == None):
            return True
		# If either one is None and the other is not, return False
        if(p == None and q != None):
            return False
        if(q == None and p != None):
            return False
        # If both are something, compare their values
        if(p != None and q!= None):
			# If the values are different, return False
            if(p.val != q.val):
                return False
            # If p and q are the same, recurse
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)