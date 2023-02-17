class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def helper(opened, closed, stack, candidate):
            if opened==0 and closed==0:
                answer.append(candidate)
                return
            if opened > 0:
                helper(opened-1,closed,stack+1,candidate+"(")
            if closed > 0 and stack>0:
                helper(opened, closed-1, stack-1, candidate+")")
        
        helper(n,n,0,"")
        return answer