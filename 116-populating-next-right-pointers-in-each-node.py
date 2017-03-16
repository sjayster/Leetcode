"""
Solution:
Based off the output, I got to know that we need to use level order traversal

1. If not root, return None
2. Have 2 arrays - parent and child and append root to the parent node
3. While parent is not empty, we need to do the following,
   a. If the length of parent[] is 1, set parent[0].next to None (as we know there is only 1 node in that level or that is the last node in that level)
   b. else, we assign parent[0].next to parent[1]
   c. Then, we add the children of parent[0] to the child array
   d. Delete the parent[0] node from the parent array
   e. If the parent is empty and if the child node is not empty, we know that we have completed one level and we need to move to the next level
   f. pop(0) all the nodes from child to parent (while child)
4. The while parent will take care of the rest.

"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if not root:
            return None
        parent = []
        child = []
        parent.append(root)
        while parent:
            if len(parent) == 1:
                parent[0].next = None
            else:
                parent[0].next = parent[1]

            if parent[0].left and parent[0].right:
                child.extend([parent[0].left, parent[0].right])
            del parent[0]
            if not parent and child:
                while child:
                    parent.append(child.pop(0))
