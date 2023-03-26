class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # check boundary and check color
        def dfs(r, c):
            if not isInbound(r, c) or image[r][c] != removed:
                return
            image[r][c] = color
            for i in range(len(direction)-1):
                dfs(r+direction[i], c+direction[i+1])
        
        removed = image[sr][sc]
        rows, cols = len(image), len(image[0])
        isInbound = lambda x,y: 0 <= x < rows and 0 <= y < cols
        direction = (1, 0, -1, 0, 1)
        
        if image[sr][sc] != color:
            dfs(sr, sc)
        
        return image
            
        
        
        