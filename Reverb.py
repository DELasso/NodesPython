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

    def traverse(self, nodo):
        if nodo:
            self.traverse(nodo.next)
            print(nodo.value)
        self.traverse(self.head)


list = LinkedList()
list.append(5)
list.append(6)
list.append(7)
list.traverse()
#5 -> 6 -> 7 -> 0
#5 -> 11 -> 18 -> 0
#Que vaya sumando cada
