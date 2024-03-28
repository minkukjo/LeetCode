class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        answer = []

        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            answer.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        answer.append(newInterval)

        while i <n:
            answer.append(intervals[i])
            i+= 1
        return answer
