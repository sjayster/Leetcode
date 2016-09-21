"""
Solution: Use 2 pointers - fast and slow in a different way - to get head start

1. Have fast and slow pointing to head
2. Iterate over the range n and move fast one step at a time
3. Once the loop ends, if fast is None, it means we need to remove the head of the list. Hence return head = head.next
4. If not, while fast.next (!), iterate slow and fast one step at a time.
5. Upon completion, slow will be 1 node away from deletion. set slow.next to slow.next.next

Example:
n = 1, list: 1-> 2-> 3-> None. 3 will be deleted
After step 2, fast will be at 2 and slow will be at 1
slow fast
1    2
2    3 (while breaks)

Set slow.next = slow.next.next => 1-> 2-> None

n = 2, list: 1-> 2-> 3-> None. 2 will be deleted
After step 2, fast will be at 3 and slow will be at 1
slow fast
1    3 (while breaks)

Set slow.next = slow.next.next => 1-> 3-> None

n = 3, list: 1-> 2-> 3-> None. 1 will be deleted
After step 2, fast will be at None and slow will be at 1
Step 3 will take place and we set head to head.next => head => 2-3-None

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if not head:
            return None
            
        slow = fast = head
        for i in xrange(n):
            if fast:
                fast = fast.next
        
        if not fast:
            head = head.next
            return head
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
            
        return head