# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Solution 1: Fast and Slow Pointer - TC: O(n), SC: O(1) 
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    # Solution 2: Double Traversal - TC: O(n), SC: O(1) 
    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        count = 0

        # First traversal to get size of list
        while dummy:
            count += 1
            dummy = dummy.next
        
        mid = count // 2 + 1

        # Second traversal to get middle node
        for i in range(mid-1):
            head = head.next

        return head