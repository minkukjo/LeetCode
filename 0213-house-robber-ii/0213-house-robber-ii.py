class Solution:
    def rob(self, nums: List[int]) -> int:
        print(nums[:-1])
        
        return max(nums[0], self.help(nums[1:]), self.help(nums[:-1]))


    def help(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0 

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2