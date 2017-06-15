"""
Binary search: Similar to find the 1st occurrence of a number
1. Set start to 0 and end to n-1
2. While start<=end, Get the mid point and see if it is a bad version
3. If isBadVersion(m) is False, set start to m+1 (as all versions prior to m are good)
4. Else, set end to m-1
5. Once the loop breaks, return start
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 0, n - 1
        while s <= e:
            m = (s + e) / 2
            if isBadVersion(m) is False:
                s = m + 1
            else:
                e = m - 1
        return s
