# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC: O(n+h), SC: O(n)
    # where n = len(nums) and h = len(head)
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookup
        numset = set(nums)

        # Create a dummy node pointing to head
        dummy = ListNode(0, head)

        # Use a pointer curr to traverse the list
        curr = dummy

        # Traverse and remove nodes whose values are in numset
        while curr.next:
            if curr.next.val in numset:
                # Delete the node by skipping it
                # ** without moving curr to next node **
                curr.next = curr.next.next
            else:
                # Move to the next node
                curr = curr.next

        # Return the modified list
        return dummy.next

    # TC: O(n+h), SC: O(n+h)
    # where n = len(nums) and h = len(head)
    def modifiedList2(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numset = set(nums)
        # dummy_node pointer precedes the head of output list
        # tail pointer always points to the curr tail of output list
        dummy_node = tail = ListNode()
        
        curr = head
        while curr:
            if curr.val not in numset:
                tail.next = ListNode(curr.val, None)
                tail = tail.next
            curr = curr.next
        
        return dummy_node.next