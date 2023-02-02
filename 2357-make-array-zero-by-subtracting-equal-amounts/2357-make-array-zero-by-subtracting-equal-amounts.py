class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_heap = [num for num in nums if num != 0]
        heapq.heapify(min_heap)
        
        operations = 0
        
        while min_heap:
            smallest = heapq.heappop(min_heap)
            temp = []
            for _ in range(len(min_heap)):
                element = heapq.heappop(min_heap)
                element -= smallest
                if element > 0:
                    temp.append(element)
            operations += 1
            for t in temp:
                heapq.heappush(min_heap, t)
                
        return operations
        
        