from typing import List
from scripts.leetcode.test import Test

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, n = 0, len(nums)
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

Test.case(lambda: Solution().removeElement([3,2,2,3], 3), 2)
Test.case(lambda: Solution().removeElement([1,0,0,1], 0), 2)
Test.case(lambda: Solution().removeElement([0,1,2,2,3,0,4,2], 2), 5)
