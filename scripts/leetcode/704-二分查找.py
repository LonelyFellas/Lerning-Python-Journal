from typing import List
from test import Test
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


s = Solution()
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], -1), 0)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], 0), 1)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], 3), 2)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], 5), 3)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], 9), 4)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], 12), 5)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], 2), -1)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], -2), -1)
Test.case(lambda: s.search([-1, 0, 3, 5, 9, 12], 13), -1)

