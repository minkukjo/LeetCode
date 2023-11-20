# Definition for singly-linked list.
from collections import defaultdict


class ListNode:
    def __init__(self, x, checked):
        self.val = x
        self.next = None
        self.visited = checked

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        checked = float('-inf')

        while head:
            if head.val == checked:
                return True
            head.val = checked
            head = head.next
            
        return False

