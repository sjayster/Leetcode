"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

My solution:
2 pointers - previous and current

1. Set previous to None, current to head
2. While current's val == item to be deleted. There are 2 conditions, 
   a) item to be deleted is either the head node or 
   b) Item is not the head node.
   
3. It is identified by using the previous pointer
   a. If previous is None, set head to current.next
   b. Set previous.next to current.next (we just bypass the cuurent node from previous)

4. If no match is found, set previous = current
5. Finally move current. current = current.next

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        previous = None
        current = head
        
        while current:
            if current.val == val:
                if not previous:
                    head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
                
            current = current.next
                
        return head