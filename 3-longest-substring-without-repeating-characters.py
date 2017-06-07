"""
Solution: A bit tough to understand

1. Define a dictionary d = {}, set i, start, m to 0 and get the length of the string
2. Iterate over the length 
3. if s[i] is in dictionary and start <= d[s[i]], set start to d[s[i]]+1
4. Else, set ans to max(ans, i-st+1) 
5. Add the char to the dictionary and update the index
6. Once the loop breaks, return ans

How it works:

s = leetcote. The max unique char is etco => 4
len(s) = 8

i   s[i]   start        if    else      ans                 d
0   l       0                 True      max(0,0-0+1)=1   {l:0
1   e       0                 True      max(1,1-0+1)=2   {l:0, e:1
2   e     d[e]+1 = 2   True             2                {l:0, e:2
3   t       2                 True      max(2,3-2+1)=2   {l:0, e:2, t:3
4   c       2                 True      max(2,4-2+1)=3   {l:0, e:2, t:3, c:4  max: "etc"
5   o       2                 True      max(3,5-2+1)=4   {l:0, e:2, t:3, c:4, o:5  max: "etco"
6   t     d[t]+1 = 4   True             4                {l:0, e:2, t:6, c:4, o:5  max: "etco"
7   e       4                 True      max(4,7-4+1)=4   {l:0, e:7, t:6, c:4, o:5  max: "tcoe"
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        i, st, ans = 0, 0, 0
        l = len(s)
        for i in xrange(l):
            if s[i] in d and st <= d[s[i]]:
                st = d[s[i]] + 1
            else:
                ans = max(ans, i - st + 1)

            d[s[i]] = i

        return ans
