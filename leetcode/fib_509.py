class Solution:
    def fib(self, N: int) -> int:
        i, j = 0, 1
        for _ in range(N):
            i, j = i + j, i
            print(i)
        return i


print(Solution.fib(1, 5))
