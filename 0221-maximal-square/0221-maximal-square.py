class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        lookup = {}
        
        def dfs(r, c):
            if r == rows or c == cols:
                return 0

            if (r,c) not in lookup:
                right = dfs(r+1, c)
                down = dfs(r, c+1)
                diagonal = dfs(r+1, c+1)
                
                # mark the current cell 0
                lookup[(r,c)] = 0
                # check the current value of the matrix
                if matrix[r][c] == '1':
                    lookup[(r,c)] = 1 + min(right, down, diagonal)
            
            return lookup[(r,c)]
        dfs(0,0)
        return max(lookup.values())**2