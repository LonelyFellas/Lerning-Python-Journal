from collections import Counter
from itertools import count
from typing import List
from scripts.leetcode.test import Test

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.sort()
        n, counter = len(nums), 0

        while n > 0 and target != 0:
            n -= 1
            remain = target - nums[n]
            target = remain
            counter += 1
            if target <= 0: return counter

        return 0 if target > 0 else counter


Test.case(lambda: Solution().minSubArrayLen(7, [2,3,1,2,4,3]), 2)
Test.case(lambda: Solution().minSubArrayLen(4, [1, 4, 4]), 1)
Test.case(lambda: Solution().minSubArrayLen(3, [1, 4, 4]), 0)
Test.case(lambda: Solution().minSubArrayLen(3, [1, 2]), 2)
Test.case(lambda: Solution().minSubArrayLen(11, [1,2,3,4,5]), 3)
Test.case(lambda: Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)
Test.case(lambda: Solution().minSubArrayLen(9, [1,3,3]), 0)
Test.case(lambda: Solution().minSubArrayLen(20, [2,16,14,15]), 2)
