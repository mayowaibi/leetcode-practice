# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC: O(n+m), SC: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()  # to initialize the linked list that will be returned
        tail = dummyNode    # to keep track of the tail (current value) at all points in the loop

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # add all the nodes from the non-empty list when all
        # the nodes from the other list has been added
        tail.next = list1 if list1 else list2

        return dummyNode.next   # return the actual combined linked list excluding the dummy node