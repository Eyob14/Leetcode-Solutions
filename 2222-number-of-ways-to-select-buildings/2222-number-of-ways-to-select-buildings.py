class Solution:
    def numberOfWays(self, s: str) -> int:
        
        count_101, count_010 = 0, 0
        count_01, count_10 = 0, 0
        count_0, count_1 = 0, 0

        for char in s:
            if char == '0':
                count_0 += 1
                count_10 += count_1
                count_010 += count_01
            else:
                count_1 += 1
                count_01 += count_0
                count_101 += count_10

        return count_101 + count_010