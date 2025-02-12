MIN, MAX = -2**31, 2**31- 1
class Solution:
    def myAtoi(self, s: str) -> int:
        temp = ""
        for i in range(len(s)):
            is_empty = temp == ""
            if is_empty and s[i] == " ":
                continue
            if is_empty and (s[i] == "-" and s[i] == "+"):
                temp += s[i]
                continue

            than = ord(s[i]) - 48
            if not 0 <= than <= 9:
                break

            temp += s[i]
        if temp == "" or temp == "-" or temp == "+":
            return 0
        res = int(temp)
        if MIN > res:
            return MIN
        elif MAX < res:
            return MAX
        else:
            return res

s = Solution()
print(+1)
# print(s.myAtoi("-42"))
# print(s.myAtoi("42"))
# print(s.myAtoi("042"))
# print(s.myAtoi(" -042"))
# print(s.myAtoi(" --042"))
# print(s.myAtoi(" -0000042"))
# print(s.myAtoi("-00000000042"))
# print(s.myAtoi("00000000042"))
# print(s.myAtoi("    00000000042"))
# print(s.myAtoi("-13337c0d3"))
# print(s.myAtoi("13337c0d3"))
# print(s.myAtoi("words and 987"))
# print(s.myAtoi("0-1"))







