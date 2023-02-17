class LRUCache:

    def __init__(self, capacity: int):
        self.collector = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.collector:
            v = self.collector[key]
            del self.collector[key]
            self.collector[key] = v
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.collector:
            del self.collector[key]
        if len(self.collector) == self.capacity:
            del self.collector[next(iter(self.collector.keys()))]
        self.collector[key] = value