class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        growth_plant = []
        for i, time in enumerate(plantTime):
            growth_plant.append((time, growTime[i]))
            
        growth_plant.sort(key=lambda t: -t[1])
        cur_time, final_time = 0, 0
        
        for plant, grow in growth_plant:
            cur_time += plant
            final_time = max(final_time, cur_time + grow)
        
        return final_time
        