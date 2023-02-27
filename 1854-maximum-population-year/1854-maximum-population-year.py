class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = {}
       
        for start, end in logs:
            people = 0
            for birth, death in logs:
                if birth <= start < death:
                    people += 1
                    
            population[start] = people
        
        max_people = max(population.values())
        answer = float("inf")
        for year, people in population.items():
            if people == max_people:
                answer = min(answer, year)
        
        return answer
        