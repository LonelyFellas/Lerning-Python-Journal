from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        flag = False


        for i in range(1, n - 1):
            if not nums[i - 1] <= nums[i] <= nums[i + 1]:
                if flag or nums[i + 1] < nums[i] < nums[i - 1]:
                    return False
                if nums[i - 1] <= nums[i + 1]:
                    nums[i] = (nums[i - 1] + nums[i + 1]) // 2
                elif nums[i] < nums[i + 1]:
                    nums[i - 1] = nums[i] - 1
                elif nums[i] > nums[i + 1]:
                    nums[i + 1] = nums[i] + 1
                flag = True
        return True

s = Solution()
# print(s.checkPossibility([4, 2, 3]))
# print(s.checkPossibility([4, 2, 3, 3]))
# print(s.checkPossibility([3, 4, 2, 3]))
# print(s.checkPossibility([1, 4, 5, 6, 8, 6, 10, 8]))
# print(s.checkPossibility([-1, 4, 2, 3]))
print(s.checkPossibility([1, 4, 1, 2]))


