from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        a = nums[0] + nums[1] + nums[2]
        min = abs(a - target)
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                dif = abs(s - target)
                if dif < min:
                    a = s
                    min = dif
                if s > target:
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    return s
        return a


print()
