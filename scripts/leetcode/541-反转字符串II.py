from typing import List


class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        ans = ""
        temp = ""
        l = len(s)
        for i in range(l):
            if int(i / k) % 2 == 0:
                temp = s[i] + temp
            else:
                if temp != "":
                    ans.join(temp)
                    temp = ""
                ans.join(s[i])
        return ans + temp
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        nums = n * n
        count = 1
        i, j = 0, 0
        direction = 0
        loop = 1

        while count <= nums:
            if  direction == 0:
                matrix[i][j] = count
                j += 1
                if j == n - loop:
                    direction = 1
            elif direction == 1:
                matrix[i][j] = count
                i += 1
                if i == n - loop:
                    direction = 2
            elif  direction == 2:
                matrix[i][j] = count
                j -= 1
                if j == loop - 1:
                    direction = 3
            elif direction == 3:
                matrix[i][j] = count
                i -= 1
                if i == loop:
                    direction = 0
                    loop += 1




            count += 1

        return matrix

    def removeDuplicates(self, nums: List[int]) -> int:

        l = len(nums)
        hd = 0
        for i in range(2, l):
            if nums[i] == nums[i + hd - 2]:
                nums[i - hd] = nums[i]
                hd += 1
                continue
            nums[i - hd] = nums[i]
        return l - hd








solution = Solution()
print(solution.removeDuplicates([1,1,1,2,2,3]))
