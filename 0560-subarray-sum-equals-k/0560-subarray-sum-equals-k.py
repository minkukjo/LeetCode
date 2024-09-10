from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        cur = 0
        ans = 0
        for i in range(len(nums)):
            cur += nums[i]

            if cur == k:
                ans += 1
            
            if cur - k in c:
                ans += c[cur-k]
            if cur in c:
                c[cur] += 1
            else:
                c[cur] = 1
        return ans
