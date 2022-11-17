class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        def dfs(node):
            if visited[node] == 1:
                return False
            
            visited[node] = 1

            for target in adj[node]:
                if visited[target] != 2 and not dfs(target):
                    return False
            
            # is it done?
            visited[node] = 2
        
            return True

        adj = {}
        visited = [0] * numCourses

        for i in range(len(prerequisites)):
            temp = []
            if prerequisites[i][0] not in adj:
                temp.append(prerequisites[i][1])
                adj[prerequisites[i][0]] = temp
                if prerequisites[i][1] not in adj:
                    adj[prerequisites[i][1]] = []
            else:
                temp.extend(adj[prerequisites[i][0]])
                temp.append(prerequisites[i][1])
                adj[prerequisites[i][0]] = temp
                if prerequisites[i][1] not in adj:
                    adj[prerequisites[i][1]] = []



        for node in adj:
            if not visited[node]:
                if not dfs(node):
                    return False

        return True