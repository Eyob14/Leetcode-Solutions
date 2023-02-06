class DetectSquares:

    def __init__(self):
        self.counter = Counter()
        

    def add(self, point: List[int]) -> None:
        self.counter[(point[0],point[1])] += 1
        

    def count(self, point: List[int]) -> int:
        result = 0
        x, y = point
        for x0, y0 in self.counter.keys():
            if abs(x-x0)-abs(y-y0) == 0 and abs(x-x0) != 0:
                result += self.counter[(x0,y0)]*self.counter[(x0,y)]*self.counter[(x,y0)]
        return result
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)