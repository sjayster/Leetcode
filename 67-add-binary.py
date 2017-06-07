"""
Solution:
1. Get the length of a and b and compute the maxlen from it.
2. Set carry to 0 and result = []
3. Iterate over range(maxlen)
   a. Set x to a[-1-i] if i< len(a) else set x to 0 (this is to pad the shorter var with 0s)
   b. Set y to b[-1-i] if i< len(b) else set x to 0 (this is to pad the shorter var with 0s)
4. s = carry + x + y
5. INSERT str(s%2) to the start of the list
6. Set carry to s/2
7. Once the loop breaks, if a carry is present, insert str(carry) to the top of the list
8. Return ''.join(result)
"""


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lena = len(a)
        lenb = len(b)
        maxlen = max(lena, lenb)
        carry = 0
        result = []

        for i in range(maxlen):
            if i < lena:
                x = int(a[-1 - i])
            else:
                x = 0

            y = int(b[-1 - i]) if i < lenb else 0

            s = carry + x + y
            result.insert(0, str(s % 2))
            carry = s / 2

        if carry:
            result.insert(0, str(carry))

        return ''.join(result)
