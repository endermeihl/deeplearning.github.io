class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:return len(nums)
        a = nums[0]
        i = 1
        while True:
            if a == nums[i]:
                nums.remove(a)
            else:
                a = nums[i]
                i += 1
            if i >= len(nums): return len(nums)


print(Solution.removeDuplicates(1,[0,0,1,1,1,2,2,3,3,4]))