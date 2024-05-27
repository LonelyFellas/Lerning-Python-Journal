import abc
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0

        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                for i3 in range(i2 + 1, n):
                    if abc(arr[i1] - arr[i2]) <= a and abc(arr[i2] - arr[i3]) <= b and abc(arr[i1] - arr[i3]) <= c:
                        ans += 1         

        return ans

s = Solution()
print(s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))   