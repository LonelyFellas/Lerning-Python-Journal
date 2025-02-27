from scripts.leetcode.test import Test

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        reverse_num = 0
        num = x
        while num > 0:
            digit = num % 10
            num = num // 10
            reverse_num = reverse_num * 10 + digit

        if x == reverse_num:
            return True

        return False


Test.case(lambda: Solution().isPalindrome(121), True)
Test.case(lambda: Solution().isPalindrome(1221), True)
Test.case(lambda: Solution().isPalindrome(1), True)
Test.case(lambda: Solution().isPalindrome(-121), False)
Test.case(lambda: Solution().isPalindrome(10), False)

