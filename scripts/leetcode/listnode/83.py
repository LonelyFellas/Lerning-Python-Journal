from typing import Optional
from base import LinkedList, ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
    
        cur = head

        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


lk = LinkedList()
lk.init_list([1, 1, 2, 3, 3])
lk.print_list()
s = Solution()
s.deleteDuplicates(lk.head)
            