class Solution:
    def tribonacci(self, N: int) -> int:
        if N <= 1: return 0
        if N == 2: return 1
        a, b, c = 0, 1, 1
        for _ in range(N - 2):
            a, b, c = b, c, a + b + c
        return c


print(Solution.tribonacci(1, 3))
