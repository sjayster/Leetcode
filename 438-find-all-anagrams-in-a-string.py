"""
Solution: Hash table - Sliding window

1. Get the length of p and s
2. Create a dictionary dp for p
3. Create a dictionary ds for s[0:len(p)]. If len(p) is 3, before entering the loop, we will have 2 elements in ds
4. Iterate over len(p)-1 to len(s)
5. Append s[i] to ds
6. Now, both len(dp) == len(ds)
7. Compare to see if dp == ds, if so, we have an anagram, store i+1-len(p) to the result array
8. Since we are simulating a sliding window, we need to get rid of the last element, ds[s[i+1-len(p)]] -=1
9. If the value is 0, we delete the key from the dict. Now we have 2 elements in ds, if the len(p) is 3

"""


class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        slen = len(s)
        plen = len(p)
        result = []
        dp = Counter(p)
        ds = Counter(s[:plen - 1])
        for i in range(plen - 1, slen):
            ds[s[i]] += 1
            if ds == dp:
                result.append(i + 1 - plen)

            ds[s[i + 1 - plen]] -= 1
            if ds[s[i + 1 - plen]] == 0:
                del ds[s[i + 1 - plen]]

        return result
