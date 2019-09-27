class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return 0
        for n in range(len(nums)):
            if nums[n] >= target: return n
        return len(nums)


print(Solution.searchInsert(1, [1, 3, 5, 6], 5))
