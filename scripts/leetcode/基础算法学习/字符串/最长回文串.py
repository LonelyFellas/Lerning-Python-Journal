from scripts.leetcode.test import Test

class Solution:
    def longestPalindrome(self, s: str) -> str:

        return ""


Test.case(lambda: Solution().longestPalindrome("ababd"), "bab")
Test.case(lambda: Solution().longestPalindrome("cbbd"), "bb")

