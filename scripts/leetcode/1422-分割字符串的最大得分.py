from test import Test


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        is_negative = n < 0
        n = abs(n)
        i = 1
        while n != 0 and n != 1:
            res *= n
            n = n >> i
            i += 1

        return float(1 / (res * x) if is_negative else res * x)







s = Solution()



Test.case(lambda: s.myPow(2.00000, 10), 1024.00000)
# Test.case(lambda: s.myPow(2.10000, 3), 9.26100)
# Test.case(lambda: s.myPow(2.00000, -2), 0.25000)