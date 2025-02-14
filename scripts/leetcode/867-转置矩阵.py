from typing import List
from scripts.leetcode.test import Test


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])

        ans = [[0 for _ in range(r)] for _ in range(c)]

        for i in range(r):
            for j in range(c):
                ans[j][i] = matrix[i][j]
        return ans


s = Solution()
Test.case(lambda: s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
Test.case(lambda: s.transpose([[1, 2, 3], [4, 5, 6], ]), [[1, 4], [2, 5], [3, 6]])

