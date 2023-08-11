class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        global_max = prev_max = prev_min = nums[0]

        for num in nums[1:]:
            curr_min = min(prev_max*num, prev_min*num ,num)
            cur_max = max(prev_min*num, prev_max*num, num)
            global_max = max(cur_max, global_max)
            prev_min = curr_min
            prev_max = cur_max
        return global_max