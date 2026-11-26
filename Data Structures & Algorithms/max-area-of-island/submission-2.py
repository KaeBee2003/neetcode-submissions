class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        l = len(grid)
        b = len(grid[0])
        def dfs(grid,i,j):
            grid[i][j] = 2
            local_area = 1
            if i < l-1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                local_area += dfs(grid,i+1,j)

            if j < b-1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                local_area += dfs(grid,i,j+1)

            if i > 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                local_area += dfs(grid,i-1,j)

            if j > 0 and grid[i][j-1] == 1:
                local_area += dfs(grid,i,j-1)

            return local_area

        for i in range(l):
            for j in range(b):
                if grid[i][j] == 1:
                    curr_area = dfs(grid,i,j)
                    max_area = max(max_area, curr_area)

        return max_area