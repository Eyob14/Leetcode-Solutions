class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)

        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        ans = 0
        queue = collections.deque([source])
        visitedStop = set()
        visitedRoute = set()
        visitedStop.add(source)

        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return ans
                for route in graph[stop]:
                    if route in visitedRoute:
                        continue
                    for newStop in routes[route]:
                        if newStop not in visitedStop:
                            queue.append(newStop)
                            visitedStop.add(newStop)
                    visitedRoute.add(route)
            ans += 1
        return -1
        