"""
Solution:
I am bad with matrix problems.
Went through this video to get an understanding of the problem:
https://www.youtube.com/watch?v=siKFOI8PNKM
"""


class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        l, t, dir = 0, 0, 0
        b, r = row - 1, col - 1
        res = []
        while t <= b and l <= r:
            if dir == 0:
                for i in range(l, r + 1):
                    res.append(matrix[t][i])
                t += 1

            elif dir == 1:
                for i in range(t, b + 1):
                    res.append(matrix[i][r])
                r -= 1

            elif dir == 2:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1

            elif dir == 3:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1

            dir = (dir + 1) % 4

        return res
