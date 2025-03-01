from typing import List
from scripts.leetcode.test import Test


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        return []

Test.case(lambda: Solution().findRightInterval([[1,2]]), [-1])
Test.case(lambda: Solution().findRightInterval([[3,4],[2,3],[1,2]]), [-1,0,1])
Test.case(lambda: Solution().findRightInterval([[1,4],[2,3],[3,4]]), [-1,2,-1])
