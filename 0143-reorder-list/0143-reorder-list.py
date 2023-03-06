# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def reverse(self, node: ListNode):
        head_next = None
        head = None
        while node != None:
            head = node
            node = head.next
            head.next = head_next
            head_next = head
        return head


    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_array = slow.next
        prev = slow.next = None
        
        while second_array:
            temp = second_array
            second_array = second_array.next
            temp.next = prev
            prev = temp
        
        first, second = head, prev
        while second:
            tmp1 , tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first ,second = tmp1, tmp2
        









