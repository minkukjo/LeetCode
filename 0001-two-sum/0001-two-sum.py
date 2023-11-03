class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = set(nums)

        for index, num in enumerate(nums):

            
            if target - num in cache:
                found_index = nums.index(target-num)
                if found_index != index:
                    return [index, found_index]
        
