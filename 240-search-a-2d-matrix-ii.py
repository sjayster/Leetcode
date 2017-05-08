"""
Solution:
a. Iterate over the sub arrays and if target in sub array, return True

b. Binary search:
Base condition: If matrix is empty or has no rows or col, return False
1. Set row to 0, rowlength = len(matrix) -1 and col to len(matrix[0]) -1
2. The condition is row <= rowlength and col >= 0, as we will be incr row and decrementing col
3. Always check to see if the target element is <, == or > than the last element of a row, 
   a. if ==, return True
   b. If lesser, then we need to check in the previous column, set col -=1
   c. If greater, we need to look in the next row, row +=1
4. Once the loop breaks, return False

"""


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or len(matrix[0]) < 1 or len(matrix) < 1:
            return False

        row = 0
        rowl = len(matrix) - 1
        col = len(matrix[0]) - 1

        while col >= 0 and row <= rowl:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1

            elif target > matrix[row][col]:
                row += 1

        return False

        """
        for m in matrix:
            if target in m:
                return True
        return False
        """
