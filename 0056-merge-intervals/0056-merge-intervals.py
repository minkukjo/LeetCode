class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        index = 0
        ans = []

        while index < len(intervals):
            
            a = intervals[index][0]
            b = intervals[index][1]
            while index < len(intervals) -1 and b >= intervals[index+1][0]:
                b = max(intervals[index+1][1], b)
                index += 1
            
            ans.append([a,b])
            index += 1
        
        return ans


    [[2,3],[4,5],[6,7],[8,9],[1,10]]
    [[1,10],[2,3],]