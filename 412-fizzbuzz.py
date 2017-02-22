"""
Simplest Solution:
Have a case for i%3, i%5, i%3 and i%5==0 and i%3 and i%5 != 0
"""


class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                result.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result
