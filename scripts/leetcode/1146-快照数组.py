from typing import List


class SnapshotArray:
    arr = []
    snap_id = -1
    map = {}
    def __init__(self, length: int):
        self.arr = [0] * length

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        arr = []
        for i in range(len(self.arr)):
            arr.append(self.arr[i])
        self.map[self.snap_id] = arr
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        arr = self.map[snap_id]
        return arr[index]




s = SnapshotArray(3)
s.set(0, 5)
id = s.snap()
print("id", id)
s.set(0, 6)
s.get(0, 0)
