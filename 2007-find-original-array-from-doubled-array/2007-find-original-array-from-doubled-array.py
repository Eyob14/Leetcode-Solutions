class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        n = len(changed)
        if n % 2 != 0:
            return []
        counts = defaultdict(int)
        for c in changed:
            counts[c] += 1
        
        original = []
        index = n-1
        while index >= 0:
            num = changed[index]
            if counts[num] == 0:
                index -= 1
            elif num % 2 != 0:
                return []
            else:
                counts[num] -= 1
                counts[num//2] -=1 
                index -= 1
                original.append(num//2)
        if len(original) == n//2:
            return original
        else:
            return []