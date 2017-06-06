"""
Solution:
1. Iterate over the row and col of grid
2. Increment count when grid[i][j] == 1
3. Nuke the lands around i, j by calling nuke(grid, i, j)
4. Once the loop breaks, return count

Nuke():
1. Base condition is to see if i,j is >=0 and <= length-1 and grid[i][j] != 0
2. Set grid[i][j] = 0
3. Recursively nuke(g, i+1, j), nuke(g, i-1, j), nuke(g, i, j+1), nuke(i, j-1) and finally return
4. The above operation will remove all the connected lands and replace it with 0
"""


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if not grid:
            return count
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    self.nuke(grid, i, j)

        return count

    def nuke(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.nuke(grid, i + 1, j)
        self.nuke(grid, i - 1, j)
        self.nuke(grid, i, j + 1)
        self.nuke(grid, i, j - 1)
        return
