from test import Test

class Solution:
    def maxScore(self, s: str) -> int:
        zero, one = 0, 0
        l = len(s)

        for i in range(l):
            if s[i] == '0':
                zero += 1
            if s[i] == '1':
                one += 1
        max_score = zero - 1 if zero >= one else one - 1
        left_score  = 0

        for i in range(l):
            if s[i] == '0' and one != 0:
                left_score += 1
                max_score = max(left_score + one, max_score)
            if s[i] == '1':
                one -= 1

        return max_score

s = Solution()

Test.case(lambda: s.maxScore("011101"),5)
Test.case(lambda: s.maxScore("00111"),5)
Test.case(lambda: s.maxScore("1111"),3)
Test.case(lambda: s.maxScore("00"),1)
Test.case(lambda: s.maxScore("000000"),5)
