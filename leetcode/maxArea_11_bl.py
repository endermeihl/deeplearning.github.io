from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                if height[i] > height[j]:
                    c = height[j] * (j - i)
                else:
                    c = height[i] * (j - i)
                if c > max: max = c
        return max


print(Solution.maxArea(1, [1, 8, 6, 2, 5, 4, 8, 3, 7]))
