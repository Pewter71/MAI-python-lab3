class MyStack:

    def __init__(self):
        self._data: list[int] = []

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> int:
        return self._data.pop()

    def top(self) -> int:
        return self._data[-1]

    def empty(self) -> bool:
        return not self._data


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
