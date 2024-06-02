from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        memory_height = height[0]
        memory_i = 0
        len_height = len(height)

        # 第一个阶段
        # 找到下坡的阶段
        is_find = False
        last_find = 0 


        # 第二个阶段
        # 找和自己平等和上坡的阶段
        memory_ans = 0
        memory_ans_i = 0
        ans = 0
        
        b_ans = 0

        i = 0
        while i < len_height:
            if not is_find:
                if last_find > height[i]:
                    is_find = True
                    memory_height = height[i - 1] 
                    memory_i = i - 1
                else:
                    last_find = height[i] 
            if is_find:
                if (memory_height < height[i]) or (memory_height == height[i] and i != memory_i): 
                    # ans += b_ans if i != len_height - 1 else  height[i] - memory_height
                    b_ans = 0
                    memory_height = height[i]
                    memory_ans = ans
                    memory_ans_i = i
                else:
                    b_ans += memory_height - height[i] 
                

                if len_height - 1 == i and memory_ans == ans and memory_i != len_height - 1 and memory_ans_i != len_height - 1:
                    i = memory_ans_i + 1
                    memory_height = height[i]
                    b_ans = 0
                    memory_ans_i = i
                    memory_i = i + 1
            i += 1
        return ans 

            
# ------------------- TEST ----------------------
s = Solution()
print(s.trap([4,2, 3]))
            
            

            

                    
            