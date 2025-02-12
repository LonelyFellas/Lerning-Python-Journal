from test import Test

class Solution:
    def myPow(self, x: float, n: int) -> float:

        return 1

s = Solution()



Test.case(lambda: s.myPow(2.00000, 10), 1024.00000)
Test.case(lambda: s.myPow(2.10000, 3), 9.26100)
Test.case(lambda: s.myPow(2.00000, -2), 0.25000)

