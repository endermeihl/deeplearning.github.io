class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = []
        for n in range(len(num1)):
            for m in range(len(num2)):
                num.append(int(num1[n]) * int(num2[m]) * 10 ** (len(num1) + len(num2) - m - n - 2))
        c = 0
        for x in num:
            c = c + x
        return str(c)


print(Solution.multiply(1, "99", "9"))
