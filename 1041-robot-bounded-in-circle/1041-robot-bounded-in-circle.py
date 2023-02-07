class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 - north
        # 1 - east
        # 2 - south
        # 3 - west
        
        pos = [0, 0]
        direction = 0
        
        for inst in instructions:
            if inst == 'G':
                if direction==0:
                    pos[1] += 1
                elif direction == 2:
                    pos[1] -= 1
                elif direction == 1:
                    pos[0] += 1
                else:
                    pos[0] -= 1
            elif inst == 'L':
                direction = (direction-1)%4
            elif inst == 'R':
                direction = (direction+1)%4
        
        if direction!=0 or pos==[0,0]:
            return True
        else:
            return False
                
        
        