"""
Solution: Using stack

1. Traverse over list1 and append all its values to stack1
2. Traverse over list2 and append all its values to stack2
3. Set a dummy node to 0, carry to 0 
4. While stack1 or stack2 is not empty, there is a possibility that stack1 might be longer than stack2
   a. If stack1 is not empty, carry += stack1.pop()
   b. if stack2 is not empty, carry += stack2.pop()
5. Now, carry might be 2 digits, like 18
6. Set dummy.val = carry %10 => 8
7. Set carry = carry/10 => 1
8. Create a new node for carry, temp = ListNode(carry)
9. temp.next = dummy => 1-> 8
10. Set dummy = temp, dummy will currently point to 1
11. Once the loop breaks, there is a possibility that dummy.val might be 0, if carry = 0, so
    If dummy.val == 0, return dummy.next else return dummy

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
        stack1 = []
        stack2 = []

        curr1, curr2 = l1, l2
        while curr1:
            stack1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next

        carry = 0
        dummy = ListNode(None)
        while stack1 or stack2:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()

            val = carry % 10
            dummy.val = val
            carry = carry / 10
            head = ListNode(carry)
            head.next = dummy
            dummy = head

        if dummy.val == 0:
            return dummy.next
        return dummy
