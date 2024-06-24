from typing import Optional

from base import LinkedList, ListNode



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prevhead = ListNode(-1) 
        prev  = prevhead 

        while list1 and list2:
            if list1.val <= list2.val:
                prev = list1
                list1 = list.next
            else:
                prev = list2
                list2 = list2.next
            prev = prev.next
        
        prev.next = list1 if list1 is not None else list2

        return prevhead.next


lk = LinkedList()
list1 = lk.init_list([1, 2, 4])
lk.print_list()
lk1 = LinkedList()
list2 = lk1.init_list([1, 3, 4])
lk1.print_list()
                
                
            
