from typing import List
from scripts.leetcode.test import Test


#TODO
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        return 0


s = Solution()
Test.case(lambda: s.maxDistance([1, 2, 3, 4, 7], 3), 3)
Test.case(lambda: s.maxDistance([5, 4, 3, 2, 1, 1000000000], 2), 999999999)
