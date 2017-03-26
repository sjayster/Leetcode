"""
Solutions:

Enhancement to the perfect square problem,

https://leetcode.com/problems/valid-perfect-square/#/description

Solution 1:
Binary search

1. Set start to 1 and end to num/2 + 1, initialize an answer variable
2. while start <= end, get the mid point
3. if mid^2 == num, return mid
4. if mid^2 > num, set end to mid -1
5. if mid^2 < num, set start to mid + 1 and set answer to mid
6. Once the loop breaks, return answer

Solution 2:
Newton's algorithm
https://discuss.leetcode.com/topic/24532/3-4-short-lines-integer-newton-every-language

1. Set answer to x 
2. While answer*answer > x, 
   set answer to 0.5 * (answer + x/answer)
3. return answer once the loop breaks

"""


class Solution(object):

    # Solution 1
    def mySqrt(self, x):
        """
        if x < 2:
            return x
        start = 1
        end = (x/2) + 1
        answer = 0
        while start <= end:
            mid = (start + end)/2
            if mid * mid == x:
                return mid

            if mid *mid > x:
                end = mid -1

            if mid * mid < x:
                start = mid + 1
                answer = mid

        return answer
        """

    # Solution 2
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x
        answer = x / 2
        while answer * answer > x:
            answer = (answer + x / answer) / 2
        return answer
