class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left = 0
        right = len(nums)-1

        ans = nums[0]

        while left < right:

            mid = (left+right) // 2
            
            ans = min(ans,nums[left], nums[right])

            if ans < nums[mid]:
                left = mid+1
            else:
                right = mid
                
        return ans