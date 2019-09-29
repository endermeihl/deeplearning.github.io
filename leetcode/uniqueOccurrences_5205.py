from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = {}
        b = set()
        for n in arr:
            if n not in a.keys():
                a[n] = 1
            else:
                a[n] = a[n] + 1
        for val in a.values():
            b.add(val)
        print(b)
        print(a)
        if len(b) == len(a): return True
        return False


print(Solution.uniqueOccurrences(1, [1, 1, 3, 3, 4, 5]))
