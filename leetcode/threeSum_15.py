from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = []
        for k in range(len(nums) - 1):
            if nums[k] > 0: return a
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    a.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return a


print(Solution.threeSum(1, [0, 0, 0]))