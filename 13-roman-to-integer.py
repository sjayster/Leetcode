"""
Solution:
1. Map all the values to a dictionary, with key being the roman and value being the integer
2. Iterate over range 0 to len-1
3. If d[s[i]] < d[s[i+1]], we need to subtract the corres value from the answer
example IV, ans = -1
4. If it is greater than d[s[i+1]], we add it to our answer
example VI, ans = 5
5. Once the loop breaks, add the value of the last element, ans += d[s[-1]]
example, IV, ans = -1 + 5 = 4; VI, ans = 5 +1 = 6

"""


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0
        length = len(s)
        for i in xrange(0, length - 1):
            if d[s[i]] < d[s[i + 1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]

        return ans + d[s[-1]]
