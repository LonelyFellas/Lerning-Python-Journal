from bisect import bisect_left
from typing import List
from scripts.leetcode.test import Test

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = []
        for nums in matrix:
            ans.extend(nums)

        pos = bisect_left(ans, target)

        return pos < len(ans) and ans[pos] == target


Test.case(lambda: Solution().searchMatrix([[1,3,5],[10,11,16,20],[23,30,34,60]], target=3), True)
Test.case(lambda: Solution().searchMatrix([[1,3,5],[10,11,16,20],[23,30,34,60]], target=13), False)
Test.case(lambda: Solution().searchMatrix([[1,3,5],[10,11,16,20],[23,30,34,60]], target=60), True)
Test.case(lambda: Solution().searchMatrix([[1,3,5],[10,11,16,20],[23,30,34,60]], target=61), False)
