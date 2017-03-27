"""
Solution:
Convert to list and reverse it using [::-1]

1. We know that there is a k value (hop) and for every 2k hop, we must reverse k positions
So the loop will iterate from 0 to len(list) with a hop of 2*k. If len = 12 and k =2, i would be 0, 4 and 8
2. Reverse i to i+k, list[4:(4+2)] to list[4:6][::-1]
3. Finally, join the list and return the result

"""


class Solution(object):

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = list(s)
        for i in range(0, len(l), 2 * k):
            l[i:i + k] = l[i:i + k][::-1]
        return ''.join(l)
