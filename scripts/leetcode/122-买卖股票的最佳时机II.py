from test import Test
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))


Test.case(lambda: Solution().maxProfit([7,1,5,3,6,4]), 7)
Test.case(lambda: Solution().maxProfit([1,2,3,4,5]), 4)
Test.case(lambda: Solution().maxProfit([7,6,4,3,1]), 0)
