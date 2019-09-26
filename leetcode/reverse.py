class Solution(object):
    def reverse(self, x):
        n = 0
        z = False
        if x > 0:
            temp = str(x)
        else:
            temp = str(abs(x))
            z = True
        re = 0
        for i in temp:
            re += int(i) * (10 ** n)
            n += 1
        if z: re *= -1
        return re


Solution.reverse(1,123)
