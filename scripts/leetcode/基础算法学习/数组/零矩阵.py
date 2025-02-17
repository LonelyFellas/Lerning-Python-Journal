from typing import List
from scripts.leetcode.test import Test

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        matrix_copy = [row[:] for row in matrix]
        for i in range(n):
            for j in range(m):
                if matrix_copy[i][j] == 0:
                    for x in range(n):
                        matrix[x][j] = 0
                    for y in range(m):
                        matrix[i][y] = 0

        print(matrix)

Solution().setZeros([
    [0, 1]
])
