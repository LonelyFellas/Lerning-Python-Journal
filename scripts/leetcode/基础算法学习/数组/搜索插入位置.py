from typing import List
from scripts.leetcode.test import Test

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

Test.case(lambda: Solution().searchInsert([1,3,5,6], 5), 2)
Test.case(lambda: Solution().searchInsert([1,3,5,6], 2), 1)
Test.case(lambda: Solution().searchInsert([1,3,5,6], 7), 4)
Test.case(lambda: Solution().searchInsert([1,3,5,6], -1), 0)
