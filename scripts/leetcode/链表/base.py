from typing import List
class ListNode:
    def __init__(self, data):
        self.val = data # 节点存储的数据
        self.next = None # 下一节点的引用，初始值为None


class LinkedList:
    def __init__(self):
        self.head = None # 链表的头节点，初始值为None
    
    def append(self, data):
        """在链表的末尾添加一个节点"""
        new_node = ListNode(data)
        if self.head is None: # 如果链表为空，新节点作为头节点
            self.head = new_node
        
        else:
            current = self.head
            while current.next: # 找到链表的末尾
                current = current.next
            current.next = new_node # 将新节点链接到末尾
    def init_list(self, arr: List[int]):
        for val in arr:
            self.append(val)
    def print_list(self):
        """打印链表中的所有节点"""
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()
