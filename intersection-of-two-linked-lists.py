"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Solution:

Idea is to make sure both the lists are of equal length, so that we can hop through it at the same time.

1. Get the length of list A and list B and the difference in lengths between both the lists.
2. If list A is longer, move list A by "difference" positions. By doing that, both the lists would have equal lengths.
3. While list A and list B are not None, traverse through the lists and compare it with each other.
4. If a match is found, return the node. If not, return None once the loop ends.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def getLength(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
            
        return count
        
    def move(self, head, diff):
        current = head
        for i in xrange(diff)
            current = current.next
            
        return current
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        length_a = self.getLength(headA)
        length_b = self.getLength(headB)
        
        if length_a > length_b:
            diff = length_a - length_b
            headA = self.move(headA, diff)
        else:
            diff = length_b - length_a
            headB = self.move(headB, diff)
            
        while headA and headB:
            if headA == headB:
                return headA
            
            else:
                headA = headA.next
                headB = headB.next
                
        return None