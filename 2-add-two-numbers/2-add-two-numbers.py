class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def set(self, val, next):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        exceeded_value = 0
        while l1 is not None or l2 is not None:

            one = 0
            if l1 is not None:
                one = l1.val
                l1 = l1.next

            two = 0
            if l2 is not None:
                two = l2.val
                l2 = l2.next

            sum_numbers = one + two
            if exceeded_value == 1:
                sum_numbers += 1
                exceeded_value = 0

            if sum_numbers >= 10:
                exceeded_value = 1
                sum_numbers -= 10

            if head is None:
                head = ListNode(sum_numbers)
            else:
                temp = head
                while temp.next is not None:
                    temp = temp.next
                temp.next = ListNode(sum_numbers)
        if exceeded_value == 1:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = ListNode(1)

        return head