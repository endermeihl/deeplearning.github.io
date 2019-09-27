from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]
        max = 0
        for i in nums:
            if max > 0:
                max += i
            else:
                max = i
            if ans < max: ans = max
        return ans


print(Solution.maxSubArray(1, [1]))
