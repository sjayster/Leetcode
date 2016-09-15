"""
My Solution: Followed the procedure for Merge sort - Turned out to be a bit long wound.

1. Have 2 objects, head and current for the new head
2. While l1 and l2 are not None, there are 3 cases:
   a. l1.val < l2.val
   b. l1.val > l2.val
   c. l1.val == l2.val
   
   If a:
    assign current.next to l1 and increment both l1 and current
   If b:
    assign current.next to l1 and increment both l1 and current
   If c:
    assign current.next to l1 and increment current, l1
    assign current.next to l2 and increment current, l2

3. Once the loop ends, check to see if l1 or l2 is still alive, if so current.next = l1 (or l2), increment l1 (or l2) and current
4. return head.next

Solution 2:

Found an awesome solution where steps 2b and 2c are combined into 1 and step 3 has been made redundant, 
https://discuss.leetcode.com/topic/21292/python-solutions-iteratively-recursively-iteratively-in-place

Here, if it is not 2a, we assign current.next to b and increment b and current.
Eventually, the values of a and b will change
Also instead of looping over step 3, we just assign current.next to l1 (or l2) whichever is present, as it has already been sorted and there is no need to compare it.

Example: l1 = 1-2-3-4 ; l2 = 1'-2'
In the first loop l1.val= 1, l2.val = 1'. else part is executed, current.next = 1', l2 => 2'
In the second loop l1.val = 1, l2.val = 2'. if is executed, 1'-1, l1 => 2
In the third loop l1.val = 2, l2.val = 2'. else is executed, 1'-1- 2' ; l2 ends, loop breaks

Simply assign current.next to l1 => 1'- 1- 2'- 2- 3

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        current = head = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
            
            
        current.next = l1 or l2
        return head.next
        
        """
        # My solution - Similar to merge sort
        
        current = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            
            elif l1.val > l2.val:
                current.next = l2
                l2 = l2.next
                
            else:
                current.next = l1
                current = current.next
                l1 = l1.next
                current.next = l2
                l2 = l2.next
            
            current = current.next
                
        while l1:
            current.next = l1
            current = current.next
            l1 = l1.next
            
        while l2:
            current.next = l2
            current = current.next
            l2 = l2.next
            
        return head.next
        """