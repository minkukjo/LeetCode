class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        temp = head

        first = temp
        second = temp.next
        first.next = second.next
        second.next = first
        head = second
        temp = first

        while temp.next != None and temp.next.next != None:         
            first = temp.next
            second = first.next
            first.next = second.next
            second.next = first
            temp.next = second
            temp = first
        return head