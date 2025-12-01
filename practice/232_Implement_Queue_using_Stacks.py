class MyQueue:

    def __init__(self):
        self._data: list[int] = []

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> int:
        a = self._data[0]
        self._data = self._data[1:]
        return a

    def peek(self) -> int:
        return self._data[0]

    def empty(self) -> bool:
        return not self._data


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
