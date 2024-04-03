class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    len1 = len(word1)
    len2 = len(word2)
    max = len2 if len1 < len2 else len1
    ans = ""
    for i in range(max): 
      if i < len1:
        ans += word1[i]
      if i < len2:
        ans += word2[i]
    return ans
  def mergeAlternately1(self, word1: str, word2: str) -> str:
    len1, len2 = len(word1), len(word2) 
    i = j = 0
    ans = list()

    while i < len1 or j < len2:
      if i < len1:
        ans.append(word1[i])
        i += 1
      if j < len2:
        ans.append(word2[j])
        j += 1
    return "".join(ans)
# ----------TEST--------------
result = Solution().mergeAlternately("abc", "pqr")
result1 = Solution().mergeAlternately1("abc", "pqr")
print(result1)