# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Two Pointer Solution - TC: O(m+n) m = list A length and n = list B length, SC: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA, listB = headA, headB

        # continue until either
        # 1. both lists intersect at a node
        # 2. both lists reach the end (no intersection)
        while headA != headB:
            headA = headA.next if headA else listB
            headB = headB.next if headB else listA
        
        return headA
