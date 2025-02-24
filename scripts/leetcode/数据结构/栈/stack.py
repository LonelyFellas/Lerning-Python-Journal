from typing import List


class Stack:
    stack = []
    def __init__(self, nums: List[int]):
        for num in nums:
            self.stack.append(num)

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def clear(self) -> None:
        self.stack = []

    def top(self) -> int:
        return self.stack[-1]


s = Stack([1, 2, 3, 4])
