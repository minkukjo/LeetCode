from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        ans = []
        for key, value in c.most_common(n= k):
            ans.append(key)
        return ans