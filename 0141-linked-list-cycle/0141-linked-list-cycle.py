

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visit = {}

        while head:
            if head.next in visit:
                return True
            else:
                visit[head.next] = head.val
            head = head.next
        return False