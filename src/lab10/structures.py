from typing import Any
from collections import deque
class Stack:

    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self,item):
        self._data.append(item)
    
    def pop(self):
        if len(self._data)!=0:
            ret = self._data[-1]
            self._data.pop()
            
        else:
            raise IndexError('Стек пуст')

        return ret
    
    def peeek(self):
        if len(self._data)!=0:
            ret = self._data[-1]            
        else:
            return None
        return ret

    def is_empty(self):
        if len(self._data)!=0:
            return False
        else:
            return True
    
    def __len__(self):
        return len(self._data)
    

class Queue:
    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Пустой")
        return self._data.popleft()

    def peek(self) -> Any | None:
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

  