# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Two Pointer Solution - TC: O(n), SC: O(1)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head.next, head.next
        totalSum = 0

        while curr:
            x = curr.val
            if x != 0:
                totalSum += x
            # if curr.val == 0, replace prev.val with sum and move its next pointer to the node after curr
            # then update prev and reset sum
            else:
                prev.val = totalSum
                prev.next = curr.next
                prev = prev.next
                totalSum = 0
            curr = curr.next

        return head.next

    # Extra Memory Solution - TC: O(n), SC: O(n-2) => O(n)
    def mergeNodes2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        curr = dummyNode

        total = 0
        head = head.next
        while head:
            # simply update total sum if value != 0
            if head.val != 0:
                total += head.val
            # else, add node containing total sum to res list and reset total to 0
            else:
                curr.next = ListNode(total, None)
                curr = curr.next
                total = 0
            # in both cases, move to next node in list
            head = head.next

        # return head of res list
        return dummyNode.next