from typing import List
from scripts.leetcode.test import Test


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return []

Test.case(lambda: Solution().twoSum([2, 7, 11, 15], 9), [1, 2])
Test.case(lambda: Solution().twoSum([2, 3, 4], 6), [1, 3])
Test.case(lambda: Solution().twoSum([-1, 0], -1), [1, 2])