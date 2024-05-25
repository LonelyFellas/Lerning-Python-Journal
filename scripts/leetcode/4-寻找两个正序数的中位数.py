from typing import List
import math

class Solution: 
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        large_len = len1 if len1 > len2 else len2
        sum_len = len1 + len2
    
        is_odd = sum_len % 2 == 0

        m1, m2 = 0, 0

        if is_odd:
            m2 = sum_len / 2
            m1 = m2 - 1
        else:
            m1 = m2 = math.floor(sum_len / 2) 
    
        i1, i2 = 0, 0
        sorttable = dict()

        for i in range(large_len + 1):
            if i > m2:
                break
            if len1 <= i1:
                sorttable[i] = nums2[i2]
                i2 += 1
            elif len2 <= i2:
                sorttable[i] = nums1[i1]
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                sorttable[i] = nums2[i2]
                i2 += 1
            else:
                sorttable[i] = nums1[i1]
                i1 += 1
        

        if not is_odd:
            return sorttable[m1] 
        return (sorttable[m1] + sorttable[m2]) / 2


# ------------------------TEST------------------------------

s = Solution()
print(s.findMedianSortedArrays([1, 3], [2])) # 2
print(s.findMedianSortedArrays([1, 2], [3, 4])) # 2.5
print(s.findMedianSortedArrays([0, 0], [0, 0])) # 0
print(s.findMedianSortedArrays([2], [1, 3])) # 2
print(s.findMedianSortedArrays([], [1])) # 1
print(s.findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1])) # 0
print(s.findMedianSortedArrays([3, 4], [])) # 3.5
print(s.findMedianSortedArrays([3], [1, 2, 4]))