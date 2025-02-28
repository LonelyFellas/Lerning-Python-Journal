from bisect import bisect_right, bisect_left
from typing import List
from scripts.leetcode.test import Test


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(bisect_left(nums[::-1], 0) for nums in grid)


Test.case(lambda: Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]), 8)
Test.case(lambda: Solution().countNegatives([[3,2],[1,0]]), 0)
