from typing import List
from scripts.leetcode.test import Test

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort(key=lambda x: x[0])
        n = len(arrays)
        min_num = arrays[0][0]


        return


Test.case(lambda: Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]), 4)
Test.case(lambda: Solution().maxDistance([[1], [1]]), 0)
