"""
Solution:
If m is [[1,2,3],[4,5,6], [7,8,9]], result should be [[7,4,1],[8,5,2],[9,6,3]]
2 steps:
1. So, the last row should become the 1st row
2. Swap m[0][1] with m[1][0] and m[0][2] with m[2][0]

So the loops would be i in range(0, len(matrix)) and j in range(i)
"""


class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
