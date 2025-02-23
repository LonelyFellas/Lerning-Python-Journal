from collections import Counter
from typing import List
from scripts.leetcode.test import Test

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        cnt = Counter()
        for word in words:
            state = 0
            for c in word:
                char = ord(c) - ord('a')
                d = 1 << char
                state |= 1 << (ord(c) - ord('a'))

            # print(state)
            res += cnt[state]
            cnt[state] += 1
        return res



# Test.case(lambda: Solution().similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]), 2)
Test.case(lambda: Solution().similarPairs(["aabb", "ab", "ba"]), 3)
