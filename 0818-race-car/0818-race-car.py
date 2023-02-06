class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        inst = 0
        
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                
                if pos == target:
                    return inst
                new_pos, new_speed = pos+speed, speed*2
                queue.append((new_pos, new_speed))
                
                if pos+speed > target and speed > 0:
                    queue.append((pos, -1))
                if pos+speed < target and speed < 0:
                    queue.append((pos, 1))
                    
            inst += 1
                