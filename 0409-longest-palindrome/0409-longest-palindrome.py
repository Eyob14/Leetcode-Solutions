class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        counter = Counter(s)
        for k, v in counter.items():
            res += 2*(v//2)
            counter[k] = v%2
        res += any(counter.values())
        return res
        