from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        result: List[List[int]] = []
        table = dict()
        max_len = 0
        index = 0
        last_num = None 

        for val in sorted_nums:
            if last_num == val: continue
            last_num = val
            num = val - 1

            if num in table:
                cur_index = table[num]
                table[val] = cur_index 
                del table[num]
                result[cur_index].append(val)
                max_len = max(max_len, len(result[cur_index]))
            else:
                table[val] = index
                result.append([val])
                max_len = max(max_len, len(result[index]))
                index += 1

        return max_len

# ----------------- TEST -----------------------
s = Solution()
# s.longestConsecutive([100,4,200,1,3,2])
s.longestConsecutive([1, 2, 0, 1])

