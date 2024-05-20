from typing import List, Dict

class Solution: 
  def twoSum(self, nums: List[int], target: int) -> List[int]:

    hashtable: Dict[int, int] = dict()
    for i, num in enumerate(nums):
      target_numb = target - num
      if target_numb in hashtable: 
        return [hashtable[target_numb], i]
      hashtable[num] = i
  
    return []

# ------------------------------Test----------------------------
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
