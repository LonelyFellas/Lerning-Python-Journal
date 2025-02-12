

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        temp_str = ""


        for i in range(len(s)):
            match_index = temp_str.find(s[i])
            if match_index == -1:
                temp_str += s[i]
            else:
                max_len = max(max_len, len(temp_str))
                temp_str = temp_str[match_index + 1:] + s[i]


        return max(max_len, len(temp_str))



s = Solution()
print(s.lengthOfLongestSubstring("aab"))