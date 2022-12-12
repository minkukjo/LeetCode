class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        array = [0] * len(nums)

        first = 0
        last = len(nums)-1

        for i, num in enumerate(nums):
            if num == 0:
                array[last] = 0
                last -= 1
            else:
                array[first] = num
                first += 1
        
        for i, num in enumerate(array):
            nums[i] = array[i]