"""
Solution: 2 pointers - Had an idea but took a while to come up with a working solution

Have 3 pointers - odd, even and evenhead
The idea is to compose all the odd and even lists separately and then link the odd with the evenhead
1. odd = head and even = evenhead = head.next. We need evenhead to mark the start of even nodes
2. While even or even.next is valid. We ignore odd because, odd.next should not be None (which would be the even node)
3. The following operations take place with the loop:
    a. odd.next = even.next
    b. odd becomes odd.next
    c. even.next = odd.next
    d. even = even.next
    
4. Finally, point odd.next to evenhead and return head

Example:

List: 1->2->3->4->5
odd = 1 even = evenhead = 2
Loop:
odd   even   odd.next = even.next odd  even.next = odd.next even
 1      2            1->3          3            2->4         4
 3      4            3->5          5            4->None     None (Loop breaks)
 
 odd.next = evenhead => 1->3->5->2->4->None
 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
            
        odd = head
        evenhead = head.next
        even = evenhead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenhead
        return head