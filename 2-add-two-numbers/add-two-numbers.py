# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            # carry is the value to be carried to the next position if sum > 10
            carry = sum // 10
            # sum holds the one-digit sum of v1 and v2 (with carry holding the other digit, if any)
            sum = sum % 10
            # add the new sum node to the new list
            curr.next = ListNode(sum)
        
            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next   