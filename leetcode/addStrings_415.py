class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        k = 0
        i = len(num1)
        j = len(num2)
        c = ""
        for n in range(0, i if i < j else j):
            if int(num1[i - n - 1]) + int(num2[j - n - 1]) + k >= 10:
                c = str(int(num1[i - n - 1]) + int(num2[j - n - 1]) + k - 10) + c
                k = 1
            else:
                c = str(int(num1[i - n - 1]) + int(num2[j - n - 1]) + k) + c
                k = 0
        if i > j:
            for n in range(i - j - 1, -1, -1):
                if int(num1[n]) + k >= 10:
                    c = str(int(num1[n]) + k - 10) + c
                    k = 1
                else:
                    c = str(int(num1[n]) + k) + c
                    k = 0
        else:
            for n in range(j - i - 1, -1, -1):
                if int(num2[n]) + k >= 10:
                    c = str(int(num2[n]) + k - 10) + c
                    k = 1
                else:
                    c = str(int(num2[n]) + k) + c
                    k = 0
        if k == 1:
            c = "1" + c
        return c


print(Solution.addStrings(1, "99", "9"))
