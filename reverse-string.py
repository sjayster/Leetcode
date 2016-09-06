"""
# Leveraging slicing operation in Python
# s[::-1] returns every character in a string starting from the last position
# string[start:end:step]. -1 represents the step and in our case it goes from the last character all the way to the 1st as we have left start and end fields as blank.
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]