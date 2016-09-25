"""
Solution: 2 pointers

1. Note: Since the 1st node could also be a duplicate. Have a dummy pointer where dummy.next = head
Have another pointer slow = dummy (0th node)
2. Set fast = head.next (2nd node)
3. Compare slow.next.val and fast.val
   a. If equal, set a flag as True
   b. If unequal,
      a. Check if the flag is set, if so, set slow.next to fast
      b. Else, move both slow and fast by 1 position
4. Finally, after the loop ends, check to see if the flag is still True, if so, assign slow.next to fast
5. return dummy.next

example: dummy/slow -> 1-1'-2-2'-2''-3-4-4'-None

slow    slow.next    fast    Flag    if    else(if)    else(else)   list
dummy        1          1'      T      √                              
dummy        1          2'      F               √                     slow.next = fast => dummy-> 2
dummy        2          2''     T      √                              
dummy        1          3       F               √                     dummy->3
dummy        3          4       F                            √ 
3            4          4'      T      √

Loop ends:
If flag:
dummy.next = fast => 3->None

Solution 2: Use while instead of if else (slight modifications to fast pointer) - Faster

1. Have 2 pointers dummy and slow, where dummy.next = head
2. Set fast to head
3. while fast is not None, 
   a. check if fast.val == fast.next.val in a while loop where fast.next is valid
      If true, keep moving fast and set the flag var to True
   b. If the values are not equal or if fast.next == None,
      1. If flag is set to True, assign slow.next = fast.next, unset flag
      2. Else, move fast and slow
4. Return dummy.next

example: dummy/slow -> 1-1'-2-2'-2''-3-4-4'-None

slow    slow.next  fast  fast.next    Flag    while    else(if)    else(else)     list
dummy        1      1        1'         T      √                              
dummy        1      1'       2          F                 √                     slow.next = fast.next => dummy-> 2
dummy        2      2'       2''        T      √                              
dummy        2      2''      3          F                 √                     dummy->3
dummy        3      3        4'         F                              √                          
3            4      4'       4''        T      √
3            4      4''      None

slow.next = fast.next => 3->None

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #solution 2:
        
        if not head or not head.next:
            return head
        
        dummy = slow = ListNode(0)
        slow.next = head
        fast = head
        flag = False
        
        while fast:
            while fast.next and fast.next.val == fast.val:
                flag = True
                fast = fast.next
                
            if flag:
                slow.next = fast.next
                fast = fast.next
                flag = False
                
            else:
                slow = slow.next
                fast = fast.next
        
        if flag:
            slow.next = fast
            
        return dummy.next
            
        """
        # Solution 1
        if not head or not head.next:
            return head
            
        dummy = slow = ListNode(0)
        slow.next = head
        
        fast = head.next
        flag = False
        
        while fast:
            if slow.next.val == fast.val:
                flag = True
                fast = fast.next
                
            else:
                if flag:
                    slow.next = fast
                    fast = fast.next
                    flag = False
                    
                else:
                    slow = slow.next
                    fast = fast.next
                    
        if flag:
            slow.next = fast
            
        return dummy.next
        """