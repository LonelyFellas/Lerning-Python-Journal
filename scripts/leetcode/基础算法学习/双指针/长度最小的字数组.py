from typing import List
from scripts.leetcode.test import Test

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return 1


Test.case(lambda: Solution().minSubArrayLen(4, [1, 4, 4]), 1)
Test.case(lambda: Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 11)