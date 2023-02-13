class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = cols = len(grid)
        isBound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        visited = set()
        direction = [(1,0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        if grid[0][0] or grid[rows-1][cols-1]:
            return -1
        
        q = deque([(0, 0, 1)])
        visited.add((0, 0))
        
        while q:
            r, c, path = q.popleft()
            
            if (r, c) == (rows-1, cols-1):
                return path
            
            for r_, c_ in direction:
                new_r = r + r_
                new_c = c + c_
                
                if isBound(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                    q.append((new_r, new_c, path+1))
                    visited.add((new_r, new_c))
            
        return -1
            
            
            
        
        