"""
Solution:

Iterative: Use a stack

1. Similar to level order traversal, stack up all the elements one level at a time.
2. Pop the top most element and check if root.left is present. 
3. We need to check to see if root.left.left and root.left.right is None.
   If so, we have our left most element, add it to answer
4. Add the left element to the stack
5. If temp.right is present, add it to the stack.
6. When the queue is empty, return the result

Recursive:

Get the left and right sum

1. Set leftsum = rightsum = 0
2. if root does not exist, return 0
3. if root has a left, 
   check to see if root.left.left is None and root.left.right is None and set leftsum to root.left.val
   else, leftsum += recurse over (root.left)

4. if root.right exists, set rightsum to recursion(root.right)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        answer = 0
        stacks = [root]
        while stacks:
            temp = stacks.pop(0)
            if temp.left:
                stacks.append(temp.left)
                if not temp.left.left and not temp.left.right:
                    answer += temp.left.val

            if temp.right:
                stacks.append(temp.right)

        return answer

    """
    def sumOfLeftLeaves(self, root):

        leftsum = rightsum = 0
        if not root:
            return 0
            
        if root.left:
            if not root.left.left:
                leftsum += root.left.val
            else:    
                leftsum += self.sumOfLeftLeaves(root.left)
            
        rightsum += self.sumOfLeftLeaves(root.right)
            
        return rightsum + leftsum
    """
