from typing import List
from scripts.leetcode.test import Test

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]





Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])