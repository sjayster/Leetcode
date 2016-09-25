"""

Solution: Similar to reverse linked list
Used a trick suggested by a friend.

1. Since the 2nd node will be the new head, save the newhead = head.next
2. Set now = head, prev = None. while now and now.next is valid
3. Assign after = now.next, afterafter = now.next.next
4. after.next = now
5. now.next = afterafter
6. if prev is valid, set prev.next = after
7. prev = now
8. now = afterafter

Finally return newhead.

Consider the list to be 1-2-3-4-5-6-None
Assume that part of the list has already been reversed. 2-1-(3-4-5-6-None)
3-4 needs to be reversed

1. Set now to 3, after = now.next (4), afterafter = now.next.next (5)
2. The list must become 4-3
   after.next = now (4-3)
3. Set 3's next to 5
   now.next = afterafter (4-3-5)
4. 1.next must be set to 4. Hence 1 must be saved in a var -> prev
   prev.next = after (1-4-3-5)
5. For the next iteration, prev = now
   now = afterafter
 
 Since we need after and afterafter, the loop must be when now and now.next are valid
 
 For the 1st iteration, prev will be None, so for step , check if prev is not None

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        now = head
        newhead = head.next
        prev = None
        
        while now and now.next:
            after = now.next
            afterafter = now.next.next
            
            after.next = now
            now.next = afterafter
            if prev:
                prev.next = after
                
            prev = now
            now = afterafter
        
        return newhead