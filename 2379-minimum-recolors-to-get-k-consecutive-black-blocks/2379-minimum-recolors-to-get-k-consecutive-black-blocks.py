class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, k
        ans, cur = float('inf'), 0
        
        for i in range(k):
            if blocks[i] == 'W':
                cur += 1
        while right < len(blocks):
            ans = min(ans, cur)
            if blocks[right] == 'W':
                cur += 1
            if blocks[left] == 'W':
                cur -= 1
            right += 1
            left += 1
        
        return min(ans, cur)