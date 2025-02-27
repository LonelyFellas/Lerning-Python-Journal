from scripts.leetcode.test import Test

MAP = {
    "}": "{",
    ")": "(",
    "]": "["
}
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        area = []
        longest , l, n =0, 0, len(s)

        for c in s:
            if c == "}" or c == ")" or c == "]":
                if len(area) == 0:
                    continue
                it = area.pop()
                if MAP[c] != it:
                    longest = max(longest, l)
                    l = 0
                    continue
                else:
                    l += 2
            else:
                area.append(c)
        print(area)

        return max(longest, l)
#
# Test.case(lambda: Solution().longestValidParentheses(s="(()"), 2)
# Test.case(lambda: Solution().longestValidParentheses(s=")()())"), 4)
# Test.case(lambda: Solution().longestValidParentheses(s="(())"), 4)
# Test.case(lambda: Solution().longestValidParentheses(s="[(())]"), 6)
# Test.case(lambda: Solution().longestValidParentheses(s="[][(())]"), 8)
# Test.case(lambda: Solution().longestValidParentheses(s=""), 0)
Test.case(lambda: Solution().longestValidParentheses(s="()(()"), 2)
