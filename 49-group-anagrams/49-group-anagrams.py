class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        result = []
        for str in strs:
            key = sorted(str)
            dic["".join(key)].append(str)
        for key in dic:
            result.append(dic[key])
        return result