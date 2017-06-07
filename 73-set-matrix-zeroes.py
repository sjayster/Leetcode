"""
Solution: Tricky problem

1. We have a flag variable that is set to True if there is a 0 in the 1st row, else we set it to False.
2. Get the number of rows and columns
3. Iterate i from 1 to row and iterate j from 0 to col
4. If m[i][j] is 0, set m[i][0] and m[0][j] as 0
5. Once the loop breaks, iterate row from 1 to row and col from col-1 to -1 (inverse)
6. If m[i][0] is 0 or m[0][j] is 0, set m[i][j] to 0
7. Once this loop breaks, if flag is True set m[0] = [0]*col -> Make first row elements 0
"""


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        flag = True if 0 in matrix[0] else False

        for i in xrange(1, row):
            for j in xrange(col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in xrange(1, row):
            for j in xrange(col - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag:
            matrix[0] = [0] * col
