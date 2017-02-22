"""
Solution:

1. Write a function to convert str to int
2. Assign n to 0. 
3. Iterate over the string and obtain the integer value by subtracting ord('0') from each character - ord_val = ord(i)-ord('0')
4. Assign it to n, n = n*10 + ord_val
5. We now have the integer value of both the strings.
6. return str(n1 + n2)
"""


class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        n1 = self.convert(num1)
        print n1
        n2 = self.convert(num2)
        print n2

        return str(n1 + n2)

    def convert(self, num):
        n = 0
        ord_val = 0
        for i in num:
            ord_val = ord(i) - ord('0')
            n = n * 10 + ord_val
        return n
