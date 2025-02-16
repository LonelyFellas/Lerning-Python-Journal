from scripts.leetcode.test import Test
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)

        left_sum, right_sum = 0, sum_nums
        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1


Test.case(lambda: Solution().pivotIndex([1,7,3,6,5,6]), 3)
Test.case(lambda: Solution().pivotIndex([2, 3,-1,8, 4]), 3)
Test.case(lambda: Solution().pivotIndex([1,2,3]), -1)
Test.case(lambda: Solution().pivotIndex([1,-1,4]), 2)
Test.case(lambda: Solution().pivotIndex([2,5]), -1)
Test.case(lambda: Solution().pivotIndex([1]), 0)
Test.case(lambda: Solution().pivotIndex([2,1,-1]), 0)
