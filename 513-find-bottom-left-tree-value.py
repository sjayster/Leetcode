"""
Solutions: Recursive and iterative

Iterative - Level order traversal, we just need to care about the 1st element in that level
1. Initialize an empty array (queue) and append root to it
2. While q is not empty, 
   a. Traverse for the length of the array (reason: we can get the number of elements in that level)
   b. temp = q.pop(0)
   c. if i == 0, we have hit the first element in that level, set answer = temp.val
3. If there is a root.left, add it to the queue
4. If there is a root.right, add it to the queue
5. Once the while breaks, return answer

Recursive:
We need a helper function to go about the problem
In the main function,
Set height to 0, initialize self.answer to None
Call helper(root, 1) -> root is at the 1st level
return self.answer

Helper(root, level):
1. If root is None, return 
2. If level > self.height, we know we have an element below the current level
   a. set self.answer to root.val
   b. set self.height to level
3. If root.left, helper(root.left, level+1)
4. If root.right, helper(root.right, level+1)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def helper(self, root, currlevel):
        if not root:
            return

        if currlevel > self.height:
            self.height = currlevel
            self.answer = root.val

        if root.left:
            self.helper(root.left, currlevel + 1)
        if root.right:
            self.helper(root.right, currlevel + 1)

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.height = 0
        self.answer = None
        self.helper(root, 1)
        return self.answer

        """
        if not root:
            return
        queue = [root]
        while queue:
            for i in range(len(queue)):
                temp = queue.pop(0)
                if i == 0:
                    answer = temp.val
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        
        return answer
        """
