class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0;
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    if j == 0:
                        res = res + 1;
                    elif grid[i][j-1] == 0:
                        res = res + 1;
                    if j == len(grid[0])-1:
                        res = res + 1;
                    elif grid[i][j+1] == 0:
                        res = res + 1;
                    if i == 0:
                        res = res + 1;
                    elif grid[i-1][j] == 0:
                        res = res + 1;
                    if i == len(grid)-1:
                        res = res + 1;
                    elif grid[i+1][j] == 0:
                        res = res + 1;
        return res;
