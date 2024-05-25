from typing import List
import math
class Solution:
  def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while right >= left:
        min_height = min(height[left], height[right])
        gap_index = right - left
        current_area = min_height * gap_index
        max_area = max(current_area, max_area) 
        if height[right] >= height[left]:
           left += 1 
        else:
           right -= 1 
    return max_area 


# ------------------- TEST-----------------------

s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))