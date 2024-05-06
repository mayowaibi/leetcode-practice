# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # List Reversal Solution - TC: O(n), SC: O(1)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        # first, reverse the list
        head = reverse(head)
        
        # then, reconstruct the list
        curr = head
        curr_max = curr.val
        while curr.next:
            if curr.next.val < curr_max:
                curr.next = curr.next.next
            else:
                curr_max = curr.next.val
                curr = curr.next
        
        # re-reverse the list before returning
        return reverse(head)
