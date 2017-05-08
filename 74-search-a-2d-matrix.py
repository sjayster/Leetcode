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
        if not matrix:
            return False
        row = 0
        rowl, col = len(matrix) - 1, len(matrix[0]) - 1

        while row <= rowl and col >= 0:
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                col -= 1

            elif matrix[row][col] < target:
                row += 1

        return False
