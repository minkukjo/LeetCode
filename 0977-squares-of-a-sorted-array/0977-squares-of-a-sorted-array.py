class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)

        answer = [0]* l

        left = 0
        right = l -1

        for i in range(len(nums)-1, -1, -1):
            left_value, right_value = nums[left]*nums[left], nums[right]*nums[right]

            if left_value < right_value:
                answer[i] = right_value
                right -= 1
            else:
                answer[i] = left_value
                left += 1

        return answer
        
        

