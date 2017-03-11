"""
Solution:

1. If it is not a happy number, we would eventually see a sum of square of an integer again over the course of the iteration.
   So have a list that stores the sum of squares.
2. For a number to be a happy number, it would eventually be 1 - this is the exit condition for our loop
3. When the number is 1, break the loop and return True
4. If not, the pythonic way to get the sum of square of the integers is to break it down to strings and get the sum.
5. We can use a for loop or a list comprehension.
   for every element in the string of numbers, compute the square of the element int(element)**2
   We will get a list with the squares, example 23 => ['2','3'] => [4, 9]. Sum of list = sum[4,9] = 13
6. We add the number to the list if it is not present, if present, return False
"""


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        s = 0
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in l:
                return False
            else:
                l.append(n)

        return True
