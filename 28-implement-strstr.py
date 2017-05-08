"""
Solution:
My original solution is the 2nd one using brute force. If there a single char match, I check to see if there others match too.

Polished solution:
Base condition: If not n, return 0. If len(needle) > len(haystack), return -1

1. get the length of needle and haystack
2. Iterate over range of haystack-needle + 1
3. Init j = 0 and while j< needle,
   a. if h[i+j] != n[j], we break
   b. If not, we increment j to see if there is a match
4. Then check to see if j = len(needle), as after a match is seen, the value of j should equal needle's length
5. If so, return i
6. Once the main for loop ends, return -1
"""


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        h = len(haystack)
        n = len(needle)
        if not n:
            return 0

        for i in range(h - n + 1):
            j = 0
            while j < n:
                if haystack[i + j] != needle[j]:
                    break
                j += 1

            if j == n:
                return i

        return -1

        """
        if not needle and not haystack or not needle and haystack:
            return 0
        
        if not haystack and needle:
            return -1
        
        ans = -1
        i, hay = 0, len(haystack)
        k, nee = 0, len(needle)

        for i in xrange(hay):
            if haystack[i] == needle[k]:
                ans = i
                s = i+1
                for k in xrange(1, nee):
                    if s >= hay:
                        return -1
                    if haystack[s] != needle[k]:
                        ans = -1
                        k = 0
                        break
                    s+=1
                if ans != -1:
                    return ans
        return ans
        """
