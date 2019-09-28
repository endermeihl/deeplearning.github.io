from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        x = ""
        for n in A:
            x += str(n)
        y = int(x) + K
        return list(i for i in str(y))


print(Solution.addToArrayForm(1, [1, 2, 0, 0], 1))
