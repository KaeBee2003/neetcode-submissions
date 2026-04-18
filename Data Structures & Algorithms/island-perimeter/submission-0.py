class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                up_also = bool(i>0 and grid[i-1][j] == 1)
                down_also = bool(i < len(grid) -1 and grid[i+1][j] == 1)
                left_also = bool(j > 0 and grid[i][j-1] == 1)
                right_also = bool(j < len(grid[0]) - 1 and grid[i][j+1] == 1)
                
                
                if grid[i][j] == 1:
                    a = a + 4
                    if up_also:
                        a = a - 1
                    if down_also:
                        a = a - 1
                    if left_also:
                        a = a - 1
                    if right_also:
                        a = a - 1
                    else:
                        pass
        return a
        