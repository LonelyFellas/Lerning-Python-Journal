from scripts.leetcode.test import Test

class Solution:
    def reverseWords(self, message: str) -> str:
        reverse_words, message = "", " " +message.strip()
        n = len(message)

        word = ""
        while n > 0:
            n -= 1
            current = message[n]

            if current == ' ':
                reverse_words += word
                if n != 0:
                    reverse_words += ' '
                word = ""

            else:
                word = current + word

        return reverse_words



Test.case(lambda: Solution().reverseWords('the sky is blue'), 'blue is sky the')
Test.case(lambda: Solution().reverseWords(' hello world '), 'world hello')
Test.case(lambda: Solution().reverseWords('a good    example'), 'example    good a')
