"""
Solution: Two pointers.
Get to mid point of the list and reverse it.

1. Have 2 pointers - fast = slow = head
2. While fast and fast.next is not None, move slow by 1 step and fast by 2 steps
3. Slow will be at the mid point of the list (if odd) or mid+1 in case of even
4. Pass slow to the reverse function and store the new head in a var. say newhead

Reverse function:
Same as reversing a linked list

5. Once you get the newhead, compare the val of head and newhead until head reaches None.
6. If there is a val mismatch, return False. Finally return True

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, slow):
        prev = None
        now = slow
        while now:
            after = now.next
            now.next = prev
            prev = now
            now = after
        
        return prev
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
            
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        newhead = self.reverse(slow)
        
        while newhead:
            if head.val != newhead.val:
                return False
            head = head.next
            newhead = newhead.next
        return True