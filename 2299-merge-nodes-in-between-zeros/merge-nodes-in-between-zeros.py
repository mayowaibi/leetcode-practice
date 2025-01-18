# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 2 Pointer Solution - TC: O(n), SC: O(1)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head.next, head.next
        totalSum = 0

        while curr:
            x = curr.val
            if x != 0:
                totalSum += x
            else:
                prev.val = totalSum
                prev.next = curr.next
                prev = prev.next
                totalSum = 0
            curr = curr.next
        return head.next