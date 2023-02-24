class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        n = len(tickets)
        steps = 0 
        i = 0
        while tickets[k] != 0:
            if tickets[i] != 0:
                tickets[i] -= 1
                steps += 1

            i = (i + 1) % n
            
        return steps