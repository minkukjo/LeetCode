from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        if amount in coins:
            return 1
        
        queue = deque([(amount,0)])
        lookup = set([amount])
        
        while queue:
            # deque.pop => pop right end from queue
            # deque.popleft => pop left end from queue
            remain, count = queue.popleft()
            print(remain)
            print(count)
            if remain == 0:
                return count
            for coin in coins:
                if remain - coin >= 0 and remain - coin not in lookup:
                    queue.append((remain-coin, count+1))
                    lookup.add(remain-coin)
        return -1


s = Solution()
result = s.coinChange([2,5,10,1],27)
print(result)