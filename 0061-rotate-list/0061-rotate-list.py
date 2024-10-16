# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None:
            return head
        if k == 0:
            return head
        
        
        temp = head

        len = 0

        while temp:
            temp = temp.next
            len += 1
            
        if len == 1:
            return head

        k = k % len
        
        if k ==0:
            return head

        dest = len - k

        temp = head

        count = 1

        while count != dest:
            temp = temp.next
            count += 1
        
        new_head = temp.next
        temp.next = None

        tail = new_head

        while tail.next:
            tail = tail.next
        tail.next = head

        return new_head
