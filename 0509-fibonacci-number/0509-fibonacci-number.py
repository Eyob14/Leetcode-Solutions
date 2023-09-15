class Solution:
    def fib(self, n: int) -> int:
        storage = {}
        def internal(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in storage:
                return storage[n]
            res = internal(n-1) + internal(n-2)
            storage[n] = res
            return res
        return internal(n)