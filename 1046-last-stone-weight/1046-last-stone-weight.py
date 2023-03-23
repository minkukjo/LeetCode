class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-stone)
        heapq.heapify(heap)
        
        while heap:
            one = -heapq.heappop(heap)
            if not heap:
                return one
            two = -heapq.heappop(heap)

            if one > two:
                heapq.heappush(heap, two-one)
        return 0
