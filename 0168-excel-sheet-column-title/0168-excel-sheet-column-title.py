class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = []

        while columnNumber > 0:
            columnNumber -= 1
            charToAdd = columnNumber%26
            columnNumber //= 26
            answer.append(chr(ord('A') + charToAdd))
            
        answer = answer[::-1]
        
        return "".join(answer)