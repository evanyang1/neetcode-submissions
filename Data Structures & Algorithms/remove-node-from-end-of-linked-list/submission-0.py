# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        dummy = ListNode()
        dummy.next = head
        cur, sz = head, 1
        while cur.next:
            cur = cur.next
            sz += 1
        removeThisNode = head
        for i in range(sz - n):
            removeThisNode = removeThisNode.next
        cur = dummy
        while cur.next != removeThisNode:
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
