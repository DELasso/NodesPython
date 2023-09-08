class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, v):
        node = Node(v)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def traverse(self):
        actual = self.head
        while actual:
            print(actual.value)
            actual = actual.next

    def del_head(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def del_tail(self):
        if self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

    def del_pos(self, position):
        if position < 0:
            return

        if position == 0:
            self.del_head()
            return

        actual = self.head
        idx = 0
        while actual and idx < position:
            actual = actual.next
            idx += 1
        if actual:
            if actual.prev:
                actual.prev.next = actual.next
            if actual.next:
                actual.next.prev = actual.prev


list = DLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)
list.traverse()
print("------------------------------------------------------")
list.del_head()
list.traverse()
print("------------------------------------------------------")
list.del_tail()
list.traverse()
print("------------------------------------------------------")
list.del_pos(2)
list.traverse()
