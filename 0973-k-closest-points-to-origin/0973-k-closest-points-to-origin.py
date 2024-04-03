class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ans = []
        l = []

        for point in points:
            dis = point[0] * point[0] + point[1] * point[1]
            l.append((dis,point[0],point[1]))
        l.sort()

        for i in range(k):
            x, y = l[i][1],l[i][2]

            ans.append([x,y])
        return ans