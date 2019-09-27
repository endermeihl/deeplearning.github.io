from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        if len(prices) == 0: return max
        buy = prices[0]
        sell = prices[0]
        for n in prices:
            if buy > n:
                buy = n
                sell = n
            if buy < n and sell < n:
                sell = n
            if sell > buy and sell - buy > max: max = sell - buy
        return max


print(Solution.maxProfit(1, [2, 4, 1]))
