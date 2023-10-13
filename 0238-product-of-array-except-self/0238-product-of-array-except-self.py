from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]

        x = 1
        for i in range(len(nums)):
            x = x * nums[i]
            prefix.append(x)
        
        postfix = deque()

        x = 1
        for i in range(len(nums)-1, -1, -1):
            x = x * nums[i]
            postfix.appendleft(x)
        postfix.append(1)

        result = []

        postfix = list(postfix)
    
        for index,val in enumerate(nums):
            sum = prefix[index] * postfix[index+1]
            result.append(sum)

        return result