class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        size = 0
        while temp is not None:
            temp = temp.next
            size += 1
        target = size - n

        if size == 1 and n == 1:
            return None
        elif target == 0:
            return head.next

        temp = head
        index = 0
        while temp is not None:
            if(index+1 == target):
                temp.next = temp.next.next
                return head
            index += 1
            temp = temp.next
        return head