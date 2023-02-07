class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for command in logs:
            if command == './':
                continue
            elif command == '../':
                count -= 1
                if count < 0:
                    count = 0
            else:
                count += 1
        return count if count > 0 else 0
            