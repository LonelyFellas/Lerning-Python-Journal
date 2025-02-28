from bisect import bisect_right, bisect_left
from typing import List
from scripts.leetcode.test import Test


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0: return [-1,-1]

        start_pos = bisect_left(nums, target)
        if start_pos < n and nums[start_pos] != target:
            return [-1,-1]
        end_pos = bisect_right(nums, target)-1
        if n > end_pos >= start_pos:
            return [start_pos, end_pos]
        return [-1, -1]


Test.case(lambda: Solution().searchRange(nums=[5,7,7,8,8,10], target=8), [3,4])
Test.case(lambda: Solution().searchRange(nums=[5,7,7,8,8,10], target=6), [-1,-1])
Test.case(lambda: Solution().searchRange(nums=[], target=0), [-1,-1])
Test.case(lambda: Solution().searchRange(nums=[2,2], target=3), [-1,-1])




