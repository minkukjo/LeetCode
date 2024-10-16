class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ans = float('inf')

        nums.sort()

        for i in range(len(nums)-2):

            l,r = i+1, len(nums)-1

            while l<r:

                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum == target:
                    return three_sum
                
                if abs(three_sum - target) < abs(ans - target):
                    ans = three_sum
                
                if three_sum < target:
                    l += 1
                else:
                    r -= 1
        return ans
