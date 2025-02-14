from test import Test
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        ans = 0
        for i in range(len(words)):
            if left <= i <= right:
                if words[i][0] in vowels and words[i][-1] in vowels:
                    ans += 1

        return ans



s = Solution()
Test.case(lambda : s.vowelStrings(["are", "amy", "u"], 0, 2), 2)
Test.case(lambda : s.vowelStrings(["hey", "aeo", "mu", "ooo", "artro"], 1, 4), 3)


