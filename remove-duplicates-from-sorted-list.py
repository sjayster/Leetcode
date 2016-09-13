"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Solution:

Straight forward traversal with 2 pointers.
1. If head or head.next is None (0 or 1 node), return head
2. Have 2 pointers (objects) current and prev. prev = head and current = prev.next and a flag to see if a dup node is seen
3. While current is not None, check for the following conditions.
   a. If prev.val == current.val
   b. If prev.val != current.val and flag is set to True
   c. If prev.val != current.val and flag is set to False
   
For 3a. Set flag to True and move the current to current.next
For 3b. All nodes from prev to current are dups, so set prev.next to current
        Set prev to current and current = current.next and reset the flag to False
        
For 3c. This is when say, nodes are unique. Simply set current to current.next and prev to prev.next

4. Finally, once we exit the loop, check to see if the flag is True. This happens when the last few nodes have equal values (1-2-2-None). In this case, we need to assign prev.next to None
   Assign prev.next = current
   
NOTE: current = current.next is a common operation and can be grouped at the end of the if..else condition.
  
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        prev = head
        current = prev.next
        dupseen = False
        while current:

            if prev.val == current.val:
                dupseen = True
                
            elif prev.val != current.val and dupseen:
                prev.next = current
                prev = current
                dupseen = False
                
            else:
                prev = prev.next
            
            current = current.next
            
        if dupseen:
            prev.next = current
        
        return head