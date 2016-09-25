"""
Solution: Similar to reverse a linked list. 
In addition to remembering prev, now and after, we need to remember the node before prev

Entry check:
1. If head or head.next does not exist, return head
2. In addition to that, if m == n, return the list as is, as no swap is required.

3. Have dummy node where dummy.next = head

Get the node before prev (mprev)
1. Assign dummy = mprev
2. Iterate mprev from i to m-1
3. mprev will point to the node before m
4. Set prev = mprev.next and now to prev.next

Reversal part:
1. Iterate over m to n
2. Set after = now.next
3. now.next = prev
4. prev = now
5. after = now

Final links:
1. If the list is 1-2-3-4-5 m = 2 and n = 4, by now the list will look like this 1(->2) 4-3-2 5
where now is 4, after = 5 and prev is 3

2. Set mprev->next->next to after (1-2-5)
3. Set mprev->next to now (1-4) => 1-4-3-2-5
4. return dummy.next

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        if not head or not head.next or m==n:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        mprev = dummy
        for i in xrange(0, m-1):
            mprev = mprev.next
            
        prev = mprev.next
        now = prev.next
        
        for i in range(m, n):
            after = now.next
            now.next = prev
            prev = now
            now = after
            
        mprev.next.next = after    
        mprev.next = prev
        return dummy.next