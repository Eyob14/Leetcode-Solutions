class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left, right = 0, len(needle)
        
        while right < len(haystack):
            if haystack[left:right] == needle:
                return left
            right += 1
            left += 1
        if haystack[left:right] == needle:
            return left
        return -1
        