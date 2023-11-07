# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_node = head = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                temp = ListNode(list1.val)
                new_node.next = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val)
                new_node.next = temp
                list2 = list2.next
            new_node = new_node.next
        
        while list1:
            new_node.next = ListNode(list1.val)
            new_node = new_node.next
            list1 = list1.next
        
        while list2:
            new_node.next = ListNode(list2.val)
            new_node = new_node.next
            list2 = list2.next
        
        return head.next