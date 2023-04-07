class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        isInbound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        visited = set()
        no_islands = 0
        
        def dfs(r, c):
            if not isInbound(r, c) or (r,c) in visited or grid[r][c] == '0':
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    no_islands += 1
                    dfs(i, j)
        
        return no_islands
        