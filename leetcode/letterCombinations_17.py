from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        x = []
        for n in digits:
            if len(x) == 0:
                x = phone[n]
                continue
            f = []
            for t in x:
                for m in phone[n]:
                    f.append(t + m)
            x = f
        return x


print(Solution.letterCombinations(1, "234"))
