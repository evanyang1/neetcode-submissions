# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        cur1 = head
        cur2 = head
        while cur1 and cur2:
            if not cur2.next or not cur2.next.next:
                return False
            if cur1.next:
                cur1 = cur1.next
            if cur2.next and cur2.next.next:
                cur2 = cur2.next.next
            if cur1 == cur2:
                return True