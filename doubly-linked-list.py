class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # ADD METHODS
    def add_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # REMOVE METHODS
    def remove_first(self):
        if self.head is None:
            return False
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return True

    # SHOWING METHODS
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        lista = []
        current = self.head
        while current is not None:
            lista.append(current.value)
            current = current.next
        print(lista)

if __name__ == '__main__':
    elementos = DoubleLinkedList()

    elementos.add_first(4)
    elementos.add_first(3)
    elementos.add_first(2)
    elementos.add_first(1)
    elementos.remove_first()
    elementos.display()
