class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        answ = True
        for i in s:
            if i in "({[":
                stack.push(i)
            else:
                if not stack.is_empty():
                    element = stack.pop()
                    if (i == ")" and element != "(") or (i == "}" and
                                                         element != "{") or (i == "]" and element != "["):
                        answ = False
                        break
                else:
                    answ = False
                    break

        if answ and stack.is_empty():
            return True
        else:
            return False


class Stack:
    def __init__(self) -> None:
        self._data: list[str] = []

    def push(self, x: str) -> None:
        self._data.append(x)

    def pop(self) -> str:

        return self._data.pop()

    def is_empty(self) -> bool:
        return not self._data
