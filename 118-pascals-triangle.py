"""
Solution:

1. Iterate over the number and append [1]*(i+1)  to the result. So for 0, there will be 1 [1]
2. If i>1, we need to manipulate the indices [2][1] to [2][j-1]
3. Iterate over range 1,i
4. Modify result[i][j] = result[i-1][j-1] + result[i-1][j] (adding the elements from the previous array and substituting it to result[i][j])
5. return result
"""


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(numRows):
            result.append([1] * (i + 1))
            if i > 1:
                for j in range(1, i):
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

        return result
