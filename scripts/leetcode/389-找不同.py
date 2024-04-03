class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    s_set = set(list(s))
    for ch in t: 
      if ch not in s_set:
        return ch
    return ''
# ----------TEST--------------
result = Solution().findTheDifference("abcd", "abcde")
print(result)