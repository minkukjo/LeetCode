class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        result = 0

        new_nums = []

        for n in nums:
            if n in numSet:
                continue
            numSet.add(n)
            new_nums.append(n)

        for n in new_nums:
            if not (n-1) in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                    result = max(length, result)
        return result
