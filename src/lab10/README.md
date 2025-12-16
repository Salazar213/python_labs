### Стек (Stack)

- **Принцип:** *LIFO* — Last In, First Out.

- **Операции:**
  - `push(x)` — положить элемент сверху;
  - `pop()` — снять верхний элемент;
  - `peek()` — посмотреть верхний, не снимая.

- **Типичные применения:**
  - история действий (undo/redo);
  - обход графа/дерева в глубину (DFS);
  - парсинг выражений, проверка скобок.

- **Асимптотика (при реализации на массиве / списке):**
  - `push` — `O(1)` амортизированно;
  - `pop` — `O(1)`;
  - `peek` — `O(1)`;
  - проверка пустоты — `O(1)`.

---

### Очередь (Queue)

- **Принцип:** *FIFO* — First In, First Out.

- **Операции:**
  - `enqueue(x)` — добавить в конец;
  - `dequeue()` — взять элемент из начала;
  - `peek()` — посмотреть первый элемент, не удаляя.

- **Типичные применения:**
  - обработка задач по очереди (job queue);
  - обход графа/дерева в ширину (BFS);
  - буферы (сетевые, файловые, очереди сообщений).

- **В Python:**
  - обычный `list` **плохо подходит** для реализации очереди:
    - удаление с начала `pop(0)` — это `O(n)` (все элементы сдвигаются);
  - `collections.deque` даёт `O(1)` операции по краям:
    - `append` / `appendleft` — `O(1)`;
    - `pop` / `popleft` — `O(1)`.

- **Асимптотика (на нормальной очереди):**
  - `enqueue` — `O(1)`;
  - `dequeue` — `O(1)`;
  - `peek` — `O(1)`.


---

### Односвязный список (Singly Linked List)

- **Структура:**
  - состоит из узлов `Node`;
  - каждый узел хранит:
    - `value` — значение элемента;
    - `next` — ссылку на следующий узел или `None` (если это последний).

- **Основные идеи:**
  - элементы не хранятся подряд в памяти, как в массиве;
  - каждый элемент знает только «следующего соседа».

- **Плюсы:**
  - вставка/удаление в **начало** списка за `O(1)`:
    - если есть ссылка на голову (`head`), достаточно перенаправить одну ссылку;
  - при удалении из середины **не нужно сдвигать** остальные элементы:
    - достаточно обновить ссылки узлов;
  - удобно использовать как базовый строительный блок для других структур
    (например, для очередей, стеков, хеш-таблиц с цепочками).

- **Минусы:**
  - доступ по индексу `i` — `O(n)`:
    - чтобы добраться до позиции `i`, нужно пройти `i` шагов от головы;
  - нет быстрого доступа к предыдущему элементу:
    - чтобы удалить узел, нужно знать его предыдущий узел → часто нужен дополнительный проход.

- **Типичные оценки:**
  - `prepend` (добавить в начало) — `O(1)`;
  - `append`:
    - при наличии `tail` — `O(1)`,
    - без `tail` — `O(n)`, т.к. требуется пройти до конца;
  - поиск по значению — `O(n)`.


### Код
`structures`

```python
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
```

`index_list`

```python
class Node:

   def __init__(self, value, next_node = None) -> None:
       self.value = value
       self.next = next_node

   def __repr__(self) -> str:
       return f"[{self.value}]"


class SinglyLinkedList:

   def __init__(self) -> None:
       self.head: Node = None
       self.tail: Node = None
       self._size: int = 0

   def append(self, value) -> None:
       new_node = Node(value)
       if self.tail is None:
           self.head = self.tail = new_node
       else:
           self.tail.next = new_node
           self.tail = new_node
       self._size += 1

   def prepend(self, value) -> None:
       new_node = Node(value, self.head)
       self.head = new_node
       if self.tail is None:
           self.tail = new_node
       self._size += 1

   def insert(self, idx: int, value) -> None:
       if idx < 0 or idx > len(self):
           raise IndexError("list index out of range")
       if idx == 0:
           self.prepend(value)
           return
       if idx == len(self):
           self.append(value)
           return
       current = self.head
       for _ in range(idx - 1):
           assert current is not None
           current = current.next
       new_node = Node(value, current.next)
       current.next = new_node
       self._size += 1

   def remove_at(self, idx: int) -> None:
       if idx < 0 or idx >= len(self):
           raise IndexError("list index out of range")
       if idx == 0:
           assert self.head is not None
           self.head = self.head.next
           if self.head is None:
               self.tail = None
           self._size -= 1
           return
       current = self.head
       for _ in range(idx - 1):
           assert current is not None
           current = current.next
       assert current is not None and current.next is not None
       current.next = current.next.next
       if current.next is None:
           self.tail = current
       self._size -= 1

   def __iter__(self):
       current = self.head
       while current:
           yield current.value
           current = current.next

   def __len__(self) -> int:
       return self._size

   def __repr__(self) -> str:
       return f"SinglyLinkedList({list(self)})"
```


Пример тетсов

![test](image.png)

Пример использования в `benchmark.py`

Как и ожидалось Stack и Queue за константное время, SinglyLinkedList односвязный список pf o(n)