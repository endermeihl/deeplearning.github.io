class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numst = list(set(nums))

        if len(numst) == 1: return numst[0]
        if len(numst) == 2:
            if numst[0] >= numst[1]:
                return numst[0]
            else:
                return numst[1]
        max = numst[0]
        max2 = numst[0]
        max3 = numst[0]
        for i in numst:
            if max <= i:
                max = i
        for i in numst:
            if max2 < i and i < max:
                max2 = i
        for i in numst:
            if max3 < i and i < max2:
                max3 = i
        return max3



print(Solution.thirdMax(1, [1,2]))
