# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = ""

        curr = head

        while curr:
            result += str(curr.val)
            curr = curr.next
        
        l = 0
        r = len(result) - 1

        while l < r:
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
        return True