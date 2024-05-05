# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # simply re-assign the val of the given node to the next node's val
        node.val = node.next.val
        # then delete the next node from the list entirely
        node.next = node.next.next
        # at the end, the VAL of the given node no longer exists in the list