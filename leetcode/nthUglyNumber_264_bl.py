class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i = 0
        temp = ugly[0]
        while len(ugly) < n:
            temp = temp + 1
            if Solution.isUgly(temp):
                ugly.append(temp)
                i += 1

        return ugly[i]

    def isUgly(num: int) -> bool:
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:
                break
        if num == 1: return True
        return False


print(Solution.nthUglyNumber(1, 100))
