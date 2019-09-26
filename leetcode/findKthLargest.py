class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kth = []
        for n in range(0, k):
            ks = 0
            kth.append(nums[0])
            for i in range(len(nums)):
                if kth[n] < nums[i]:
                    kth[n] = nums[i]
                    ks = i
            if len(nums) > ks: nums.pop(ks)
        return kth[k - 1]


print(Solution.findKthLargest(1, [5, 2, 4, 1, 3, 6, 0], 4))
