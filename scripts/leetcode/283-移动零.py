from scripts.leetcode.test import Test
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        count = 0
        i = 0
        while i < n-count:
            if nums[i] == 0:
                count += 1
                i += 1
                continue
            nums[i], nums[i-count] = nums[i-count], nums[i]
            i += 1

Test.case(lambda: Solution().moveZeroes([0,1,0,3,12]), None)
# Test.case(lambda: Solution().moveZeroes([0]), None)