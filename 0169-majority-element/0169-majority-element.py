from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        max_item = c.most_common(n=1)

        return max_item[0][0]