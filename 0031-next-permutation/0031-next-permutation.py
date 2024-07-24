class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(nums, index1, index2):
            temp = nums[index1]
            nums[index1] = nums[index2]
            nums[index2] = temp
        
        a = len(nums)-2
        while a >= 0 and nums[a] >= nums[a+1]:
            a-=1
        
        if a != -1:
            b = len(nums)-1
            while b > 0 and nums[a] >= nums[b]:
                b -=1
            swap(nums,a,b)
        start = a+1
        end = len(nums)-1
        while start < end:
            swap(nums,start, end)
            start+=1
            end-=1