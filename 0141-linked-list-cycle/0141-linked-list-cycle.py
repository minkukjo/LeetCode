# Definition for singly-linked list.
from collections import defaultdict


class ListNode:
    def __init__(self, x, checked):
        self.val = x
        self.next = None
        self.visited = checked

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
            
        return False

