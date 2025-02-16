from test import Test

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 3 or x == 2:
            return 1
        left, right, ans = 2, x // 2, -1
        while left <= right:
            mid = left + (right - left) // 2
            if mid**2 <= x:
                ans = mid
                left = mid + 1
            elif mid**2 > x:
                right = mid - 1
            else:
                return mid
        return ans

Test.case(lambda: Solution().mySqrt(2147483647), 46340)
Test.case(lambda: Solution().mySqrt(4), 2)
Test.case(lambda: Solution().mySqrt(8), 2)
Test.case(lambda: Solution().mySqrt(9), 3)
Test.case(lambda: Solution().mySqrt(10), 3)
Test.case(lambda: Solution().mySqrt(16), 4)
Test.case(lambda: Solution().mySqrt(17), 4)
Test.case(lambda: Solution().mySqrt(24), 4)
Test.case(lambda: Solution().mySqrt(25), 5)
Test.case(lambda: Solution().mySqrt(26), 5)
Test.case(lambda: Solution().mySqrt(36), 6)
Test.case(lambda: Solution().mySqrt(37), 6)
Test.case(lambda: Solution().mySqrt(100), 10)
Test.case(lambda: Solution().mySqrt(90), 9)
