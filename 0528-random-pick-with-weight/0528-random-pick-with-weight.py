class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.nums = w
    def pickIndex(self) -> int:
        index = random.randint(1, self.nums[-1])
        answer = bisect.bisect_left(self.nums, index)
        
        return answer
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()