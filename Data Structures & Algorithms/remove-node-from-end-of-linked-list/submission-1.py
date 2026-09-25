# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        len = 1
        while curr.next != None:
            curr = curr.next
            len += 1

        if n == len:
            return head.next
        
        prev = head
        for _ in range(len - n - 1):
            prev = prev.next
        curr = prev.next
        if len>1:
            nxt = curr.next

        if len>1:
            curr.next = None
            prev.next = nxt
        else:
            head = None
        return head
