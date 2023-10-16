class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        
        if len(num_set) == 1:
            return 1

        max_len = 0

        for i, value in enumerate(nums):

            if value -1 not in num_set:
                length = 0
                while (value + length) in num_set:
                    length += 1
                max_len = max(max_len, length)
        
        return max_len
