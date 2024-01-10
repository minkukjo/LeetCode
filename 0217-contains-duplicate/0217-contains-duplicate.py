from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        c = Counter(nums)

        for value in c:
            if c[value] > 1:
                return True
        return False