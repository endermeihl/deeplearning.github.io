from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        res = 0
        for a in A:
            for b in B:
                for c in C:
                    for d in D:
                        if a + b + c + d == 0: res += 1
        return res

print(Solution.fourSumCount())
