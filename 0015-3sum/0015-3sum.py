class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = set()


        for i in range(len(nums)):

            if i>=1 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1

            while l < r:

                m = nums[i] + nums[l] + nums[r]

                if m > 0:
                    r -= 1
                elif m < 0:
                    l += 1
                else:

                    v = tuple([nums[i], nums[l], nums[r]])

                    if v not in ans:
                        ans.add(v)
                    l += 1
                    r -= 1
                
        return ans