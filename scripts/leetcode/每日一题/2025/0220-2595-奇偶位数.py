from typing import List
from scripts.leetcode.test import Test

class Solution:
    def evenOddBit(self, num: int) -> List[int]:
        binary_str = bin(num)[2:]
        even, odd = 0, 0

        for index, char in enumerate(binary_str[::-1]):
            if char == '1':
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1

        return [even, odd]


Test.case(lambda: Solution().evenOddBit(num=50), [1, 2])
Test.case(lambda: Solution().evenOddBit(num=2), [0, 1])



