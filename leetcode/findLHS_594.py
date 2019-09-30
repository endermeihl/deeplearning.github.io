from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}
        for item in nums:
            if item not in hashmap:
                hashmap[item] = 1
            else:
                hashmap[item] += 1
        res = 0
        for item in hashmap:
            if item+1 in hashmap:
                up = hashmap[item+1]
                res = max(res,up+hashmap[item])
        return res


print(Solution.findLHS(1, [1, 3, 2, 2, 5, 2, 3, 7]))
