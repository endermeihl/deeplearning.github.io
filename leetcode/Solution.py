class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in range(0, len(nums)):
            for m in range(n + 1, len(nums)):
                temp = nums[n] + nums[m]
                if temp == target:
                    return [n, m]
        return None
