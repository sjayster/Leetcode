"""
Solution: Same as merging two lists

1. Have 2 objects, head and current for the new head
2. Have a carry an total variable set to 0
3. While l1 and l2 are not None, there are 3 cases:
   total = l1.val + l2.val + carry
   current.next = ListNode(total%10) - This will create a new node for the last digit in carry
   For the subsequent rounds, carry = carry/10 -> This has the leftover carry digits
   
4. Once the loop ends, check to see if l1 or l2 is still alive, if so repeat the above steps
5. Check to see if carry is 0, if so, until carry is 0, keep repeating step 3
6. return head.next

Solution 2:

The above code can be simplified by using if statements.
We know that the same set of operations are being carried out while l1, l2, carry is valid.
1. Create head and current nodes and assign total = 0
2. Hence, while l1 or l2 is valid,
   a. if l1 is valid, set total += l1.val and move l1
   b. if l2 is valid, set total += l2.val and move l2
3. set current.next to ListNode(total%10) and move current
4. total = total/10
5. Once both l1 and l2 are None, check to see if total is 0.
6. If not, keep adding current.next(total%10) and total/=10 and move current
7. return head.next

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """        
        current = head = ListNode(0)
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            current.next = ListNode(carry%10)
            current = current.next
            carry /= 10
            
        while carry:
            current.next = ListNode(carry%10)
            current = current.next
            carry /= 10
            
        return head.next
        
        """
        
        current = head = ListNode(0)
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total/10
            total %= 10
            current.next = ListNode(total)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry
            carry = total/10
            total %= 10
            current.next = ListNode(total)
            current = current.next
            l1 = l1.next
            
        while l2:
            total = l2.val + carry
            carry = total/10
            total %= 10
            current.next = ListNode(total)
            current = current.next
            l2 = l2.next
        
        while carry:
            current.next = ListNode(carry%10)
            carry /= 10
            current = current.next
            
        return head.next