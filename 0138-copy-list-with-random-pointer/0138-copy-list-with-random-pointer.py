# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        map = defaultdict()

        temp = head

        while temp:
            map[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head


        while temp:
            n = map[temp]
            if temp.next == None:
                n.next = None
            else:
                n.next = map[temp.next]
            
            if temp.random == None:
                temp.random = None
            else:
                n.random = map[temp.random]
            
            temp = temp.next
        
        return map[head]