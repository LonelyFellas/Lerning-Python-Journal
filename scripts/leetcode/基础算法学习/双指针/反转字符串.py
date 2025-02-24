from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        ptr1, ptr2 = 0, len(s) - 1
        while ptr1 < ptr2:
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1
