"""
Solution:

1. Have a list answer = [-inf, -inf, -inf]
2. Iterate over the number list. If the number is not in answer, 
a. If num > answer[0], recreate answer = [num, answer[0], answer[1]]
b. else if num > answer[1], recreate answer = [answer[0], num, answer[1]]
c. else if num > answer[2], recreate answer = [answer[0], answer[1], num]
3. Once the loop breaks, if answer doesn't have -inf in it, return v[2] else return max(answer)
"""


class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        answer = [float('-inf'), float('-inf'), float('-inf')]

        for num in nums:
            if num not in answer:
                if num > answer[0]:
                    answer = [num, answer[0], answer[1]]
                elif num > answer[1]:
                    answer = [answer[0], num, answer[1]]
                elif num > answer[2]:
                    answer = [answer[0], answer[1], num]
        print answer
        if float('-inf') in answer:
            return max(answer)
        return answer[2]
