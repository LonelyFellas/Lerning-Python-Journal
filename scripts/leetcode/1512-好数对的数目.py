from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table = dict()
        ans = 0

        for i, val in enumerate(nums):
            if val in table:
                table[val] += 1
            else:
                table[val] = 1

        for val in table:
            if val > 1:
                cur = val - 1
                while cur >= 1:
                    ans += cur 
                    cur -= 1

        return ans


s = Solution()
print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
