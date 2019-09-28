from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = 1
        for n in range(len(digits) - 1, -1, -1):
            if digits[n] + k == 10:
                digits[n] = 0
                k = 1
            else:
                digits[n] = k + digits[n]
                k = 0
        if k == 1:
            digits = [1] + digits
        return digits


print(Solution.plusOne(1, [9, 9, 9]))
