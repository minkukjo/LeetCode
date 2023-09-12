class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a,b,c = target

        maxA, maxB, maxC = 0,0,0
        for i,j,k in triplets:
            if i <= a and j <= b and k <= c:
                maxA = max(maxA, i)
                maxB = max(maxB, j)
                maxC = max(maxC, k)
        return maxA == a and maxB == b and maxC == c
