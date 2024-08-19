from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        m = defaultdict(int)

        for num in nums:
            m[num] = 1
        
        m_len = 0
        for num in nums:
            cur_l = 1

            if num -1 in m:
                continue

            while cur_l + num in m:
                cur_l += 1
            m_len = max(m_len, cur_l)
        
        return m_len

