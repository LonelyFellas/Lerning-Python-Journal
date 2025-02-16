from typing import List
from scripts.leetcode.test import Test

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先按起始位置排序
        intervals.sort(key=lambda x: x[0])
        ans = []
        ans.append(intervals[0])
        n = 0

        for i in range(1, len(intervals)):
            if ans[n][1] < intervals[i][0]:
                ans.append(intervals[i])
                n += 1
            elif intervals[i - 1][0] <= ans[n][1] < intervals[i][1]:
                ans[n][1] = intervals[i][1]
        return ans


Test.case(lambda: Solution().merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6], [8,10], [15,18]])
Test.case(lambda: Solution().merge([[1,4],[4,5]]), [[1,5]])
Test.case(lambda: Solution().merge([[1,4,],[0,4]]), [[0,4]])
