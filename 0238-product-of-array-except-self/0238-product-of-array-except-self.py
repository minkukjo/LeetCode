class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        first = [1] * (len(nums))

        first[0] = nums[0]

        second = [1] * (len(nums))

        second[-1] = nums[-1]


        for i in range(1, len(nums)):
            first[i] = first[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            second[i] = second[i+1] * nums[i]

        for i in range(len(nums)):

            left = 1
            if i-1 >= 0:
                left = first[i-1]

            right = 1
            if i+1 < len(nums):
                right = second[i+1]
            
            nums[i] = left* right

        return nums