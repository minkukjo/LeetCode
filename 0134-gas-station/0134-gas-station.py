class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        trip_tank = 0
        cur_tank = 0
        start = 0
        n = len(gas)
        for i in range(n):
            trip_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]

            if cur_tank < 0:
                start = i+ 1
                cur_tank = 0
        return start if trip_tank >= 0 else -1