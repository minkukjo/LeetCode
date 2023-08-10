from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # queue with current amount and number of coins
        q = deque([(amount,0)])
		
		# set with visited amount to avoid duplicate work
        visited = set()

        while q:
            amount, sum = q.popleft()

            if amount == 0:
                return sum
            
            for c in coins:
                new_amount = amount - c

                if new_amount in visited or new_amount <0 :
                    continue

                q.append((new_amount,sum+1))
                visited.add(new_amount)
        return -1



