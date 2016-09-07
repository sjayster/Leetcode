"""
My Solution:

1. Using a dictionary
Iterate over s and add it to a dictionary
Iterate over t and keep decrementing the count if an element is present in the dictionary else return if the element is not present in the dictionary or if count <= 0

Thought of using XOR but didn't know how to proceed.
Found this solution here, https://discuss.leetcode.com/topic/55930/1-liners-python-ruby
Subtract the sum of ord(t) and ord(s). Convert it to char

"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        d = {}
        
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in t:
            if i not in d or d[i] <= 0:
                return i
            else:
                d[i] -= 1
        """        
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
        """