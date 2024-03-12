# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 2 pointer linked list solution
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        l = dummyNode
        r = head

        # offsetting r by n nodes from the head
        for i in range(n):
            r = r.next

        # traverse through the list 
        # (until l is at the node before the node to be deleted and r has passed the final node)
        while r:
            l, r = l.next, r.next

        # removing the node after l (nth node from end of the list)
        l.next = l.next.next

        return dummyNode.next