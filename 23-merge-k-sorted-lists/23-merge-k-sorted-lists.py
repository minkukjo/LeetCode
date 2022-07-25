class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = []
        
        for list in lists:
            while list:
                sorted_list.append(list.val)
                list = list.next
        
        sorted_list = sorted(sorted_list)

        result = head = ListNode()
        
        for val in sorted_list:
            head.next = ListNode(val)
            head = head.next

        return result.next