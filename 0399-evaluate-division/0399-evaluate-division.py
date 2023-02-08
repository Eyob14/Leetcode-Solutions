class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        for idx, equation in enumerate(equations):
            x, y = equation
            graph[x][y] = values[idx]
            graph[y][x] = 1 / values[idx]
            
        for key in graph.keys(): 
            graph[key][key] = 1
        
        def dfs(node1, node2, visited):
            visited.add(node1)
            for child in graph[node1].keys():
                if child == node2: 
                    return graph[node1][node2]
                elif child not in visited:
                    res = dfs(child, node2, visited)
                    if res >= 0: 
                        return res * graph[node1][child]
            return -1
        
        answer = []
        for x, y in queries:
            answer.append(dfs(x,y,set()))
            
        return answer
        
            
        