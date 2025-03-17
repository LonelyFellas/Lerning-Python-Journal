from scripts.leetcode.test import Test

MAP = {
    "1": "I",
    "4": "IV",
    "5": "V",
    "9": "IX",
    "10": "X",
    "40": "XL",
    "50": "L",
    "90": "XC",
    "100": "C",
    "400": "CD",
    "500": "D",
    "900": "CM",
    "1000": "M",
}

class Solution:
    def inToRoman(self, num: int) -> str:
        res = ""
        count = 0
        while num > 0:
            digit = num % 10
            num //= 10
            count +=1
            if digit in MAP:
                res += MAP[digit]
                continue

            if count == 1:
                if digit >= 5:
                    d = digit
                    d -= 5






        return ""


Test.case(lambda: Solution().inToRoman(3749), "MMMDCCXLIX")
