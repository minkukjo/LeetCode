class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def topoSort(V, arr):
                # Code here
                n= V
                ind=[0]*n
                q=[]
                for i in range(n):
                    for j in arr[i]:
                        ind[j]+=1
                for i in range(n):
                    if ind[i]==0:
                        q.append(i)
                if  len(q)==0:
                    return False
                cnt=0
                while q:
                    item=q.pop(0)
                    cnt+=1
                    for i in arr[item]:
                        ind[i]-=1
                        if ind[i]==0:
                            q.append(i)       
                return cnt==numCourses
        graph = {node: [] for node in range(numCourses)}
        for seq in prerequisites:
            preq, course = seq[0], seq[1]
            graph[course].append(preq)
        return topoSort(numCourses,graph)