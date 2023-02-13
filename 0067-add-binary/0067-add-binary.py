class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = 0 
        i, j = len(a), len(b)
        for n in a:
            i -= 1
            num += (int(n) * 2 ** i)
        for n in b:
            j -= 1
            num += (int(n) * 2 ** j)
        return ((str(bin(num))[2::]))
          