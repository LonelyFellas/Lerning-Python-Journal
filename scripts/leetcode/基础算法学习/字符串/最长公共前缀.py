from typing import List
from scripts.leetcode.test import Test

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""


        break_flag = False
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                n = len(strs[j])
                if i + 1 > n or strs[j][i] != c:
                    break_flag = True
            if break_flag:
                break
            common += c

        return common









Test.case(lambda: Solution().longestCommonPrefix(["flower", "flow", "flight"]), "fl")
Test.case(lambda: Solution().longestCommonPrefix(["dog", "racecar", "car"]), "")
