from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)

        count = 0
        for num in nums:
            count += num - min_num

        return count


s = Solution()
print(s.minMoves([1, 2, 3]))