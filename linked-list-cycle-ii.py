"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

Solution:

Extension of Linked list cycle problem.
To identify linked list cycle, we make use of 2 objects, fast and slow, where fast moves 2 steps at a time and slow moves one step at a time.

In this problem, once both fast and slow meet, we reset the position of fast to head and move both fast and slow, one node at a time. It would definitely meet after k steps (where k is the number of nodes before the start of the cycle)

Good explanations:
https://discuss.leetcode.com/topic/5284/concise-o-n-solution-by-using-c-with-detailed-alogrithm-description
https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def culprit(self, slow, fast):
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return fast
        
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                fast = head
                return self.culprit(slow, fast)
                
        return None