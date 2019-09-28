class Solution:
    def addBinary(self, a: str, b: str) -> str:
        k = 0
        i = len(a)
        j = len(b)
        c = ""
        for n in range(0, i if i < j else j):
            if int(a[i - n - 1]) + int(b[j - n - 1]) + k == 2:
                c = "0" + c
                k = 1
            elif int(a[i - n - 1]) + int(b[j - n - 1]) + k == 3:
                c = "1" + c
                k = 1
            else:
                c = str(int(a[i - n - 1]) + int(b[j - n - 1]) + k) + c
                k = 0
        if i > j:
            for n in range(i - j - 1, -1, -1):
                if int(a[n]) + k == 2:
                    c = "0" + c
                    k = 1
                else:
                    c = str(int(a[n]) + k) + c
                    k = 0
        else:
            for n in range(j - i - 1, -1, -1):
                if int(b[n]) + k == 2:
                    c = "0" + c
                    k = 1
                else:
                    c = str(int(b[n]) + k) + c
                    k = 0
        if k == 1:
            c = "1" + c
        return c


print(Solution.addBinary(1, "10", "10000110"))
