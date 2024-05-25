from typing import List
class Solutaion: 
   def three_Sum(self, nums: List[int]) -> List[List[int]]:
      ans = []

      settable = set(nums)


      for item1 in settable:
        temp_set = {item1}
        for item2 in settable:
            if item2 != item1: 
                temp_set.add(item2)
                for item3 in settable:
                    if item1 != item2 != item3 and (item1 + item2 + item3) == 0:
                        temp_set.add(item3)

                        ans.append(list(temp_set))

        




      return ans
      
s = Solutaion()
result = s.three_Sum([-1, 0, 1, 2, -1, 4])

print(result)