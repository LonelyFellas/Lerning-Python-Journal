from typing import List
from test import Test


class Solution:
    def peekIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)




        return 1


s = Solution()
Test.case(lambda: s.peekIndexInMountainArray([0, 1, 0]), 1)
Test.case(lambda: s.peekIndexInMountainArray([0, 2, 1, 0]), 1)
Test.case(lambda: s.peekIndexInMountainArray([0, 10, 5, 2]), 1)

