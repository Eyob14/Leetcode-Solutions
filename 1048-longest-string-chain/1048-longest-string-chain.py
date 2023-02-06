class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        def predecessor(prev, curr):
            if abs(len(curr)-len(prev)) != 1:
                return False                    
            i = j = 0
            mismatched = 0
            while i < len(prev):
                if prev[i] == curr[j]:
                    j += 1
                    i += 1
                else:
                    if mismatched:
                        return False
                    mismatched = True
                    j += 1
            return True
        
        @cache
        def dfs(idx):
            if idx == len(words):
                return 1
            
            max_val = 1
            for i in range(idx, len(words)):
                if i + 1 < len(words) and predecessor(words[idx], words[i + 1]):
                    max_val = max(max_val, dfs(i + 1) + 1)
            return max_val

        res = 1
        for i in range(len(words)):
            res = max(res, dfs(i))
    
        return res
        