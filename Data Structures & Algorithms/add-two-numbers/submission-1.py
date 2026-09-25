# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_digit(LL):
            curr = LL
            mul = 10
            val = curr.val
            while curr.next != None:
                curr = curr.next
                val = val + mul*curr.val
                mul = mul * 10
            return val

        val = get_digit(l1) + get_digit(l2)
        
        if val == 0:
            digits = [0]
        else:
            digits = []
            while val != 0:
                digits.append(val%10)
                val = val // 10

        head = ListNode()
        curr = head
        for i in digits:
            curr.next = ListNode(val = i)
            curr = curr.next

        return head.next



            