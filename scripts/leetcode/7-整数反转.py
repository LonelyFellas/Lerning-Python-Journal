

MIN = -2 ** 31
MAX = 2 ** 31

class Solution:
    def reverse(self, x: int) -> int:
        f = x < 0
        digit_str = str(x)
        digit_str = digit_str[1:]  if f else digit_str
        reversed_str = digit_str[::-1]
        reversed_int = int(("-" if f else "") + reversed_str)
        if MIN <= reversed_int <= MAX:
            return reversed_int
        return 0

    def reverse_str(self, s: str) -> str:
        p1 = 0
        p2 = len(s) - 1
        s_list = list(s)
        while p1 < p2:
            s_list[p1], s_list[p2] = s_list[p2], s_list[p1]
            p1 += 1
            p2 -= 1
        return "".join(s_list)


s = Solution()
print(s.reverse(-123))
print(s.reverse(210))
print(s.reverse(0))
print(s.reverse(-1))
print(s.reverse(1534236469))
