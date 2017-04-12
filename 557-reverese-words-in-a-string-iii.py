"""
Solution:

Break it down to lists and reverse every element of the list
Return ' '.join(list)

Can be shortened using map(function, s.split)
where function is lambda x: x[::-1]
"""


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = s.split()
        for i in range(len(res)):
            res[i] = res[i][::-1]

        return ' '.join(res)

        # return ' '.join(map(lambda x: x[::-1], s.split(' ')))
