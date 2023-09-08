class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, v):
        node = Node(v)

        if not self.head:
            self.head = node
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = node

    def traverse(self):
        stack = []
        actual = self.head
        while actual:
            stack.append(actual.value)
            actual = actual.next

        while stack:
            print(stack.pop())

list = LinkedList()
list.append(4)
list.append(6)
list.append(9)

list.traverse()
