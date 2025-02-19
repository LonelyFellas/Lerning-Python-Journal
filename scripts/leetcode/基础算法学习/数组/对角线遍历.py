from typing import List
from scripts.leetcode.test import Test


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        lines = m + n - 1
        ans = [0] * (m * n)

        x, y = 0, 0
        count = 0
        for i in range(lines):
            while i % 2 == 0:
                ans[count] = matrix[x][y]
                count += 1

                if y == n - 1:
                    x += 1
                    break
                elif x == 0 :
                    y += 1
                    break
                else:
                    x -= 1
                    y += 1
            while i % 2 != 0:
                ans[count] = matrix[x][y]
                count += 1
                if x == m - 1:
                    y += 1
                    break
                elif y == 0:
                    x += 1
                    break
                else:
                    x += 1
                    y -= 1
        return ans




Test.case(lambda: Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])