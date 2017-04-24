"""
Solution:

Create 2 lists, one lesser than x and one greater than x and then combine the two.

1. Create 2 list heads, littlehead and bighead with 0 as its value 
2. Set newhead as littlehead and in order to combine the lists, we need the head of bighead, assign bighead to original_bighead
3. While current is not None, compare current.val with x
   a. If it is less than x, create a new node to littlehead.next
   b. If it is greater than x, create a new node to bighead.next
   c. set current to current.next
   
4. Once the loop breaks, littlehead and bighead would be in the last node of its corresponding lists.
5. Set littlehead.next to original_bighead.next (as original_bighead has been initalized with 0)
6. Return newhead.next (as newhead points to littlehead(0) and we need the value from after that)

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        current = head
        littlehead = ListNode(0)
        bighead = ListNode(0)
        original_bighead = bighead
        newhead = littlehead

        if not head or not head.next:
            return head

        while current:
            if current.val < x:
                littlehead.next = ListNode(current.val)
                littlehead = littlehead.next

            else:
                bighead.next = ListNode(current.val)
                bighead = bighead.next

            current = current.next

        littlehead.next = original_bighead.next
        return newhead.next
