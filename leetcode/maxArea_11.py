from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max = max(min(height[left], height[right]) * (right - left), max)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max


print(Solution.maxArea(1, [1, 8, 6, 2, 5, 4, 8, 3, 7]))
