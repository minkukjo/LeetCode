class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        
        ans = set()
        nums.sort()
        for i in range(len(nums)):

            if i>=1 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                middle = nums[i] + nums[l] + nums[r]

                if middle > 0:
                    r -= 1
                elif middle < 0:
                    l += 1
                else:
                    target = tuple([nums[i], nums[l], nums[r]])

                    if target not in ans:
                        ans.add(target)
                    
                    l += 1
                    r -= 1
        return ans
