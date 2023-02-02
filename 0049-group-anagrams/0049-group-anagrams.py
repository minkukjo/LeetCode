class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for str in strs:
            
            sorted_str = sorted(str)
            dic[tuple(sorted_str)].append(str)

        return list(dic.values())
