# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC: O(n), SC: O(1)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head

        while curr.next:
            newNode = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr.next = newNode
            curr = curr.next.next
        
        return head