class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degree_count = [0]*n
        
        for initial, destination in edges:
            degree_count[destination] += 1
        
        answer = []
        for vertex, degree in enumerate(degree_count):
            if degree == 0:
                answer.append(vertex)
        return answer