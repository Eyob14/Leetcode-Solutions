class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mapper = defaultdict(set)
        for Id, time in logs:
            mapper[Id].add(time)
            
        ans = [0] * k
        for Id, value in mapper.items():
            ans[len(value) - 1] += 1
            
        return ans