from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visit = set()
        def dfs(node):
            if node in visit:
                return []
            
            visit.add(node)
            result = [node]

            for element in adj[node]:
                result += dfs(element)
            return result

        adj = defaultdict(set)
        name_dic = defaultdict()

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                adj[acc[1]].add(email)
                adj[email].add(acc[1])
                name_dic[email] = name

        ans = []

        for email in adj:
            if email not in visit:
                v = name_dic[email]
                ans.append([v]+ sorted(dfs(email)))
        return ans


        