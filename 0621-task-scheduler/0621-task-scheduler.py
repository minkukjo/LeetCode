class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = Counter(tasks)
        max1 = max(a.values())
        counter = 0
        for i in a.values():
            if i == max1:
                counter = counter + 1
        result = (max1 - 1) * (n + 1) + counter
        return max(result, len(tasks))