from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        que = PriorityQueue()

        for point in points:
            
            value = (point[0] * point[0]) + (point[1] * point[1])
            que.put((value,point[0],point[1]))
        
        
        ans = []
        i = 0
        while i < k:
            value, point[0], point[1] = que.get()
            ans.append([point[0],point[1]])
            i += 1
        return ans

