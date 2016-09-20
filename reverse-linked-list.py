"""
My solution:

Iterative approach:

For the reversal of linked list, we need 3 pointers (objects in Python):
now -> points to the current node
before -> points to now-1 node
after -> points to the now+1 node

1. Initialize now to the head, before as None 
2. While now is not None, we perform the foll operations:
   a. Assign after = now.next
   b. now.next = before
   c. before = now
   d. now = after
   
3. Finally, assign head = before and return head.

Example: 1-> 2-> 3-> None
head = 1
before  now   after   new-list 
None     1      2     1-> None 2->3->None
1        2      3     2->1->None 3->None 
2        3    None    3->2->1->None 
3       None

Recursive:

Couldn't come up with a proper recursive code. Found this solution on the discuss page.
https://discuss.leetcode.com/topic/17916/8ms-c-iterative-and-recursive-solutions-with-explanations

1. The base condition is to see if head or head.next is None. If so, return head
2. If not, call reverse(head.next) and assign it to a Node object.
   n = reverese(head.next)
3. Assign head.next.next to head
4. Assign head.next to None

Example: 1-> 2-> 3-> None

a. n = rev(1)
b.   n = rev(2)
c.     n = rev(3) -> base condition is hit, return 3 and exit c
b continues: 2.next.next = 2 (3.next = 2) 3-2
             2.next = None 3- 2- None
b ends, a continues
1.next.next = 1 => 2.next = 1 => 3-2-1
1.next = None => 3-2-1-None

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Iterative:
        
        now = head
        before = None
        
        while now:
            after = now.next
            now.next = before
            before = now
            now = after

        head = before
        return head
        
        """
        # Recursive
        
        if not head or not head.next:
            return head
        
        n = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return n
        
        """