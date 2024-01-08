# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0

        temp = head

        while temp:
            temp = temp.next
            length += 1
            
        mid = length // 2
        target_index = mid+1
        
        temp = head
        index = 1
        while index != target_index:
            temp = temp.next
            index += 1
        

        return temp