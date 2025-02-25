from rest_framework.fields import empty

from scripts.leetcode.test import Test

MAP = {
   "}": "{",
    ")": "(",
    "]":"["
}
class Solution:
    def isValid(self, s: str) -> bool:
        area = []

        for c in s:
            if c == "}" or c == ")" or c == "]":
                if len(area) == 0:
                    return False
                it = area.pop()
                if MAP[c] != it:
                    return False
            else:
                area.append(c)

        return len(area) == 0



Test.case(lambda: Solution().isValid("()"), True)
Test.case(lambda: Solution().isValid("()[]{}"), True)
Test.case(lambda: Solution().isValid("(]"), False)
Test.case(lambda: Solution().isValid("([])"), True)
Test.case(lambda: Solution().isValid("([)]"), False)


