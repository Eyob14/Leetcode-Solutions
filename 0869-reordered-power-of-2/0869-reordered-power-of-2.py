class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def powerOfTwo(n):
            if n == 1:
                return True
            if n == 0:
                return False
            if n % 2 == 0:
                return powerOfTwo(n/2)
        num = str(n)
        for x in itertools.permutations(num):
            number = "".join(list(x))
            if x[0] != '0':
                if powerOfTwo(int(number)) == True:
                    return True
        return False
        