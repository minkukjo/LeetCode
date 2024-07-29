from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for str in strs:
            d[''.join(sorted(str))].append(str)
        return d.values()