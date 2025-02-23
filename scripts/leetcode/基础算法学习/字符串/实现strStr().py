from scripts.leetcode.test import Test

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n > h:
            return -1
        e, i, temp, res = 0, 0, -1, -1

        while i < h:
            if haystack[i] == needle[e]:
                e += 1
                if temp == -1:
                    temp = i
            elif e != 0:
                e = 0
                i = temp
                temp = -1

            if e >= n:
                res = temp
                break

            i +=1
        return res

# Test.case(lambda: Solution().strStr('sadbutsad', 'sad'), 0)
# Test.case(lambda: Solution().strStr('sadbutsad', 'sadbutsad'), 0)
# Test.case(lambda: Solution().strStr('sadbutsad', 'sadbutsad1'), -1)
# Test.case(lambda: Solution().strStr('sadbutsad', 'but'), 3)
# Test.case(lambda: Solution().strStr('sadbutsad1', 'ad1'), 7)
# Test.case(lambda: Solution().strStr('leetcode', 'leeto'), -1)
# Test.case(lambda: Solution().strStr('mississippi', 'issip'), 4)
# Test.case(lambda: Solution().strStr('mississippi', 'issipi'), -1)
Test.case(lambda: Solution().strStr('aaaa', 'baaa'), -1)
