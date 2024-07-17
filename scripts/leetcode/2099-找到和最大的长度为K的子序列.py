from typing import List 
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        
        count = k
        res: List[int] = []
        for i in nums[::-1]:
            res.append(i)

            count -= 1
            if count <= 0:
                break
        
        return res 
            
          

#------------------- TEST -----------------
s = Solution()
print(s.maxSubsequence([3, 4, 3, 3], 2))