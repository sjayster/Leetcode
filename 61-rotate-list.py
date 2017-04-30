"""
Solution: Two solutions - 
1. Get the length and traverse through the array
2. Make the linked list as a circular one and then manipulate.

Solution 1:
1. Get the length of the list and save it to count
2. Since k can be larger than count, set k <- k%count
3. Assign a dummy, slow and fast pointer to head
4. Iterate fast over range count-k.
5. While fast.next is not None, set slow to prev, move slow and fast by one position
6. Once the loop breaks, slow is our new head fast will be at None-1 position
7. Set fast.next to dummy and prev.next to None
8. Return new head

Solution 2:
The above solution can be simplified to just one pass by using the same fast and slow pointer logic.

1. While fast.next is valid, keep incrementing count
2. When the loop breaks, set fast.next to head to make this a circular linked list
3. Set k to k%count
4. For i in range(count-k), move fast by one position.
5. At the end of the iteration, fast.next will be our new head.
6. Set newhead to fast.next, set fast.next = None
7. return newhead
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Solution 2:
        if not head:
            return None

        slow = fast = head
        count = 1

        while fast.next:
            count += 1
            fast = fast.next

        fast.next = head

        k = k % count

        for i in range(count - k):
            fast = fast.next

        newhead = fast.next
        fast.next = None
        return newhead

        """
        # Solution 1:
        
        if not head:
            return None
        count = 0
        counter = head
        while counter:
            count +=1
            counter = counter.next
        
        if k%count == 0:
            return head
            
        k = k%count

        fast = slow = dummy = head
        for i in range(1,k):
            fast = fast.next
        
        prev = None
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next

        newhead = slow
        prev.next = None
        fast.next = dummy
        
        return newhead
        """
