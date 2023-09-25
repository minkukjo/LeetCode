class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        min = intervals[0][0]
        max = intervals[0][1]

        ans = [[min, max]]
        for index, arr in enumerate(intervals):
            if index == 0:
                continue

            if min <= arr[0] and max >= arr[0]:
                ans.pop()
                max = arr[1] if arr[1] > max else max
                ans.append([min,max])
            else:
                ans.append(arr)
                min = arr[0]
                max = arr[1]
        return ans