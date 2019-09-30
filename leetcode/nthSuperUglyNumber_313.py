from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primes.sort()
        ugly = [1]
        a = []
        for z in range(len(primes)):
            a.append([primes[z], 0])
        while len(ugly) < n:
            # 找到需要*2, *3, *5的最小索引(i2, i3, i5不会越界)
            for k in range(len(a)):
                while ugly[a[k][1]] * a[k][0] <= ugly[-1]:
                    a[k][1] += 1
            temp = min(ugly[t[1]] * t[0] for t in a)
            ugly.append(temp)

        return ugly[-1]


print(Solution.nthSuperUglyNumber(1, 12, [2, 7, 13, 19]))
