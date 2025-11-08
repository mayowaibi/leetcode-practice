# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC: O(n+h), SC: O(n+h)
    # where n = len(nums) and h = len(head)
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
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