from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: List[List[str]] = []
        temptalbe = dict()
        count = 0
        
        
        for val in strs:
            sortedVal = ''.join(sorted(val))
            getVal = temptalbe.get(sortedVal)
            if getVal != None:
                result[getVal].append(val)
            else:
                temptalbe[sortedVal] = count
                result.append([val])
                count += 1
        
        return result
                 

# ----------------- TEST ------------------------
s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
                        
