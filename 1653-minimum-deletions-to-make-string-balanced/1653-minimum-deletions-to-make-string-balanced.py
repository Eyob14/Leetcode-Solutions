class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        stack = []
        
        for c in s:
            if c == "a":
                if stack:
                    stack.pop()
                    ans += 1
            else:
                stack.append(c)
                
        return ans
        