from scripts.leetcode.test import Test

def computed(i: int) -> int:
    if i <= 9:
        return i
    r = 0
    while i > 0:
        r += i % 10
        i = i // 10

    return r

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        area = [0] * (highLimit + lowLimit)
        max_n = 0

        for i in range(lowLimit, highLimit + 1):
            res = computed(i)
            area[res-1] += 1
            max_n = max(max_n, area[res-1])

        return max_n


s = Solution()
# Test.case(lambda: s.countBalls(1, 10), 2)
# Test.case(lambda: s.countBalls(5, 15), 2)
# Test.case(lambda: s.countBalls(19, 28), 2)
# Test.case(lambda: s.countBalls(11, 104), 9)
Test.case(lambda: s.countBalls(4, 7), 1)






