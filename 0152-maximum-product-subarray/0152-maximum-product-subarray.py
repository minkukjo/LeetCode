class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min1 = nums[0]
        max1 = nums[0]

        result = nums[0]

        for i in range(1,len(nums)):
            temp = max1
            max1 = max(nums[i], nums[i]*max1, nums[i]*min1)
            min1 = min(nums[i], nums[i]*temp, nums[i]*min1)
            result = max(max1,result)
        return result