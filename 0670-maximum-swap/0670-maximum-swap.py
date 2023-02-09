class Solution:
    def maximumSwap(self, num: int) -> int:
        number = list(str(num))
        answer = num
        
        for i in range(len(number)):
            for j in range(i+1, len(number)):
                number[i], number[j] = number[j], number[i]
                new_num = "".join(number)
                answer = max(answer, int(new_num))
                number[i], number[j] = number[j], number[i]
        
        return answer
                
        
        
        