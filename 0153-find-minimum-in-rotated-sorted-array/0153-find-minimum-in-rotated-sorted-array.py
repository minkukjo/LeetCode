class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r = 0, len(nums)-1

        ans = nums[0]
        while l<r:

            mid = (l+r) // 2
            
            ans = min(ans, nums[l], nums[r])

            if ans < nums[mid]:
                l = mid+1
            else:
                r = mid
        
        return ans

