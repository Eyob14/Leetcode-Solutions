class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        answer = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                current_cell = 0
                start = 0 if i-k < 0 else i-k
                end = rows if i+k+1 > rows else i+k+1
                for cur in range(start, end):
                    temp_sum = sum(mat[cur][max(0, j-k): min(cols, j+k+1)])
                    current_cell += temp_sum
                    answer[i][j] = current_cell
        return answer
        