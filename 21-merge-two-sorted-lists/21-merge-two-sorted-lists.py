
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        temp = result
        while list1 != None and list2 != None:
            
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        
        while list1 != None:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
        
        while list2 != None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next

        return result.next
