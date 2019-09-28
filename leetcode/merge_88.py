from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        nums1[:] = []
        i = 0
        j = 0
        while j < m and i < n:
            if nums2[i] > nums1_copy[j]:
                nums1.append(nums1_copy[j])
                j += 1
            else:
                nums1.append(nums2[i])
                i += 1
        if j < m:
            nums1[j + i:] = nums1_copy[j:]
        if i < n:
            nums1[j + i:] = nums2[i:]

        return nums1


print(Solution.merge(1, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
