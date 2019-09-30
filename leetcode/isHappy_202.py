class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            x = 0
            for i in str(n):
                x += int(i) ** 2
                n = x
            if x == 1:
                return True
            if x in visited:
                return False
            visited.add(n)


print(Solution.isHappy(1, 19))
