class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = list1
        second = list2
        new = ListNode()

        while first != None and second != None:

            val = first.val
            if first.val <= second.val:
                first = first.next
            else:
                val = second.val
                second = second.next
            
            temp = new
            while temp.next != None:
                temp = temp.next
            temp.next = ListNode(val)
        
        if first != None:
            temp = new
            while temp.next != None:
                temp = temp.next
            temp.next = first
        if second != None:
            temp = new
            while temp.next != None:
                temp = temp.next
            temp.next = second
        return new.next