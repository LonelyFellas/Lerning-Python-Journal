from typing import List
from scripts.leetcode.test import Test

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        res, count = 0, 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0 or (nums[i] == 1 and i == n - 1):
                res = max(res, count)
                count = 0

        return res


Test.case(lambda: Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)
Test.case(lambda: Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2)

