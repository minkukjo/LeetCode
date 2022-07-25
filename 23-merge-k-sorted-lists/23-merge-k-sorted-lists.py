class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self,lists:List[ListNode])->ListNode:
        data = []
        for list in lists:
            while list:
                data.append(list.val)
                list = list.next
        data = sorted(data)
        root = temp = ListNode()
        for i in data:
            temp.next = ListNode(i)
            temp = temp.next
        return root.next