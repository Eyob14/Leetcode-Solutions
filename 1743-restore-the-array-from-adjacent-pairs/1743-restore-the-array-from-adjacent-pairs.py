class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mapper = defaultdict(list)
        for parent, child in adjacentPairs:
            mapper[parent].append(child)
            mapper[child].append(parent)
        
        start = 0
        for key, value in mapper.items():
            if len(value) == 1:
                start = key
                break

        answer = []
        def dfs(cur, parent):
            answer.append(cur)
            for value in mapper[cur]:
                if value != parent: 
                    dfs(value, cur)
        
        dfs(start, None)
        
        return answer
            
        
        