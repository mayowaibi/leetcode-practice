# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        curr = dummyNode
        carry = 0   # to store any value that needs to be carried to the next node

        while l1 or l2 or carry:
            # v1 and v2 are the corresponding values from each linked list
            # set to 0 if any of the linked lists are null
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            totalSum = v1 + v2 + carry
            carry = totalSum // 10  # to get the carry digit if sum > 10
            totalSum = totalSum % 10    # to ensure sum only holds the unit place value of totalSum
            
            curr.next = ListNode(totalSum)   # add the new initialized sum node to the list

            # update all pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyNode.next   # return the entire list