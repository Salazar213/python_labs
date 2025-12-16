import time
import random

class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if len(self._data) != 0:
            return self._data.pop()

class Queue:
    def __init__(self):
        from collections import deque
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.popleft()

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

print("="*50)
print("ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ДАННЫХ")
print("="*50)

sizes = [100, 1000, 10000]

test_data = {}
for size in sizes:
    test_data[size] = [random.randint(1, 1000) for _ in range(size)]

print("\n1. Stack (стек)")
print("-"*30)

for size in sizes:
    print(f"\nРазмер: {size} элементов")
    
    s = Stack()
    data = test_data[size]
    
    start = time.perf_counter()
    for item in data:
        s.push(item)
    push_time = time.perf_counter() - start
    
    start = time.perf_counter()
    for _ in range(size):
        s.pop()
    pop_time = time.perf_counter() - start
    
    print(f"  Push: {push_time:.6f} сек ({push_time/size*1e6:.2f} µs на элемент)")
    print(f"  Pop:  {pop_time:.6f} сек ({pop_time/size*1e6:.2f} µs на элемент)")

print("\n" + "="*50)
print("\n2. Queue (очередь)")
print("-"*30)

for size in sizes:
    print(f"\nРазмер: {size} элементов")
    
    q = Queue()
    data = test_data[size]
    
    start = time.perf_counter()
    for item in data:
        q.enqueue(item)
    enqueue_time = time.perf_counter() - start
    
    start = time.perf_counter()
    for _ in range(size):
        q.dequeue()
    dequeue_time = time.perf_counter() - start
    
    print(f"  Enqueue: {enqueue_time:.6f} сек ({enqueue_time/size*1e6:.2f} µs на элемент)")
    print(f"  Dequeue: {dequeue_time:.6f} сек ({dequeue_time/size*1e6:.2f} µs на элемент)")

print("\n" + "="*50)
print("\n3. SinglyLinkedList (односвязный список)")
print("-"*30)

for size in sizes:
    print(f"\nРазмер: {size} элементов")
    
    lst = SinglyLinkedList()
    data = test_data[size]
    
    start = time.perf_counter()
    for item in data:
        lst.append(item)
    append_time = time.perf_counter() - start
    
    print(f"  Append: {append_time:.6f} сек ({append_time/size*1e6:.2f} µs на элемент)")

print("\n" + "="*50)
print("ВЫВОДЫ:")
print("-"*30)

print("""
1. Stack (стек):
   - Push: O(1) - время на операцию не зависит от размера
   - Pop:  O(1) - время на операцию не зависит от размера

2. Queue (очередь):
   - Enqueue: O(1) - время на операцию не зависит от размера  
   - Dequeue: O(1) - время на операцию не зависит от размера

3. SinglyLinkedList (односвязный список):
   - Append: O(n) - время растёт с ростом размера,
     т.к. нужно пройти весь список до конца
""")