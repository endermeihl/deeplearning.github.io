from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min = abs(nums[0] + nums[1] + nums[2] - target)
        a = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            for n in range(i + 1, len(nums) - 1):
                for m in range(n + 1, len(nums)):
                    if abs(nums[i] + nums[m] + nums[n] - target) == 0:
                        return nums[i] + nums[m] + nums[n]
                    elif abs(nums[i] + nums[m] + nums[n] - target) < min:
                        min = abs(nums[i] + nums[m] + nums[n] - target)
                        a = nums[i] + nums[m] + nums[n]
        return a


print(Solution.threeSumClosest(1, [-1, 2, 1, -4], 1))
