# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp_l1 = l1
        temp_l2 = l2
        while temp_l1.next != None or temp_l2.next != None:
            if temp_l1.next == None:
                temp_l1.next = ListNode()
            temp_l1 = temp_l1.next

            if temp_l2.next == None:
                temp_l2.next = ListNode()
            temp_l2 = temp_l2.next


        head = ListNode()
        temp = head
        upper = 0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + upper
            if sum >= 10:
                temp.next = ListNode(sum - 10)
                upper = 1
            else:
                temp.next = ListNode(sum)
                upper = 0
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        if upper == 1:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = ListNode(1)

        return head.next


