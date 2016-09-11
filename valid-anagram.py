"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

1. Simplest solution is to see whether sorted(s) == sorted(t). All the elements will be in ascending order.
By comparing the sorted strings we will know if all the characters in s are present in t. If not, return false.

2. Using hash table  Straight-forward implementation.
Add all elements to the dictionary with the char as key and occurrence as the value.
Iterate over list 2 and keep subtracting the value for the char.
If count < 0 or sum(values) != 0, return False 

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in t:
            if i not in d or d[i] <= 0:
                return False
            else:
                d[i] -= 1
        
        return sum(d.values()) == 0
        
        """
        return sorted(s) == sorted(t)
        """