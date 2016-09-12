"""
Given a linked list, determine if it has a cycle in it.

Solution:

To identify linked list cycle, we make use of 2 objects, fast and slow, where fast moves 2 steps at a time and slow moves one step at a time.

1. Set slow = fast = head
2. while fast.next or fast.next.next (odd/even length list) is not None
   a. Move slow = slow.next
   b. fast = fast.next.nexy.
3. Check if slow == fast
   a. If a cycle is present, both the nodes will eventually meet at some point and we can return true when it happens
   b. If no cycle is present, the fast node will reach None ahead of the slow and we can return False

Another awesome use of Python:

https://discuss.leetcode.com/topic/16098/except-ionally-fast-python
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return False

        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False