class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left = 1
        right = x // 2

        while left < right:
            mid = (left + right + 1) // 2
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        return left

    def judgeSquareSum(self, c: int) -> bool:
        seq = self.mySqrt(c)
        i = 0
        j = seq
        while i <= j:
            if i ** 2 + j ** 2 == c: return True
            if i ** 2 + j ** 2 > c: j -= 1
            if i ** 2 + j ** 2 < c: i += 1
        return False
