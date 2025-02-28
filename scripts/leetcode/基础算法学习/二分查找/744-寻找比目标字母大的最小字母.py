from bisect import bisect_right
from typing import List
from scripts.leetcode.test import Test

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]


#
Test.case(lambda: Solution().nextGreatestLetter(["c", "f", "j"], "a"), "c")
Test.case(lambda: Solution().nextGreatestLetter(["c", "f", "j"], "c"), "f")
Test.case(lambda: Solution().nextGreatestLetter(["c", "f", "j"], "j"), "c")
Test.case(lambda: Solution().nextGreatestLetter(["c", "f", "j"], "f"), "j")
Test.case(lambda: Solution().nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")
Test.case(lambda: Solution().nextGreatestLetter(["x", "x", "y", "y"], "y"), "x")
Test.case(lambda: Solution().nextGreatestLetter(["x", "x", "y", "y"], "x"), "y")
Test.case(lambda: Solution().nextGreatestLetter(["x", "x", "x", "x"], "x"), "x")
Test.case(lambda: Solution().nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"), "n")
