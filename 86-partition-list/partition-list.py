# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Partition List Solution - TC: O(n), SC: O(1)
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lDummy, rDummy = ListNode(), ListNode()
        lTail, rTail = lDummy, rDummy

        # assign nodes to separate left and right lists
        # representing nodes with vals < x and >= x respectively
        while head:
            if head.val < x:
                lTail.next = head
                lTail = lTail.next
            else:
                rTail.next = head
                rTail = rTail.next
            head = head.next

        # connect left to right and make right point to null
        lTail.next = rDummy.next
        rTail.next = None

        return lDummy.next