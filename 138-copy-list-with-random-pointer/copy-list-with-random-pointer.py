"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Optimal Interleaving Solution - TC: O(n), SC: O(1)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 1. Create a copy of every node in list and insert it right after its original
        l1 = head
        while l1:
            l2 = Node(l1.val)  # Create a new copy node
            l2.next = l1.next  # Point the copy to the next original node
            l1.next = l2  # Insert the copy right after the original
            l1 = l2.next  # Move to the next original node
        
        newHead = head.next  # head of copied list is the node after original head
        
        # 2. Assign random pointers from the original to the copy nodes
        l1 = head
        while l1:
            if l1.random:
                l1.next.random = l1.random.next  # Assign random pointer for the copy
            l1 = l1.next.next  # Move to the next original node
        
        # 3. Separate the original and copy list
        l1 = head
        while l1:
            l2 = l1.next  # Get copy node
            l1.next = l2.next  # Restore the original list's next pointer
            if l2.next:
                l2.next = l2.next.next  # Move the copied list forward
            l1 = l1.next  # Move to the next original node
            
        return newHead

    # One-pass Hashmap Solution - TC: O(n), SC: O(n)
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = defaultdict(lambda: Node(0))  # setting default value for each key to be a new node
        old_to_copy[None] = None  # ensuring that if None is accessed as a key, None is returned

        curr = head
        while curr:
            old_to_copy[curr].val = curr.val
            old_to_copy[curr].next = old_to_copy[curr.next]
            old_to_copy[curr].random = old_to_copy[curr.random]
            curr = curr.next
        
        return old_to_copy[head]
