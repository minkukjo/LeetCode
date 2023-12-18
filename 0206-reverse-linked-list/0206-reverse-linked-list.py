# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        temp = head

        next_node = None
        while temp:

            new_node = temp
            temp = temp.next
            new_node.next = next_node
            next_node = new_node
        return new_node
