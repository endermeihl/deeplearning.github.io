from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a = set()
        nums.sort()
        for k in range(len(nums) - 3):
            for h in range(k + 1, len(nums) - 2):
                left, right = h + 1, len(nums) - 1
                while left < right:
                    s = nums[k] + nums[h] + nums[right] + nums[left]
                    if s < target:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                    elif s > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
                    else:
                        a.add((nums[k], nums[h], nums[right], nums[left]))
                        left += 1
                        right -= 1
        return [list(z) for z in a]

print(Solution.fourSum(1, [0, 0, 0, 0], 0))
