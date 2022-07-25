class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = sorted_list = ListNode()

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            val, index, node = heapq.heappop(heap)
        
            sorted_list.next = node
            sorted_list = sorted_list.next
            if sorted_list.next:
                heapq.heappush(heap, (sorted_list.next.val, index, sorted_list.next))


        return result.next