class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def search(start, end):

            if start > end:
                return None

            mid = (start + end) // 2

            root = TreeNode(nums[mid])
            root.left = search(start, mid-1)
            root.right = search(mid + 1, end)
            return root
        return search(0, len(nums)-1)