# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Fast + Slow Pointer Solution - TC: O(n), SC: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. get to the middle of list
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # after loop terminates, slow points to the
        # first element after the middle of the list
        
        # 2. reverse second half of list
        prev, curr = None, slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # after loop terminates, prev points
        # to the head of the reversed second half

        # 3. compare first half and reversed second half
        list1 = head
        list2 = prev

        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return True

    # List + Two-Pointer Solution - TC: O(n), SC: O(n)
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        num_list = []
        curr = head

        while curr:
            num_list.append(str(curr.val))
            curr = curr.next
        
        l = 0
        r = len(num_list) - 1

        while l < r:
            if num_list[l] != num_list[r]:
                return False
            l += 1
            r -= 1
        return True