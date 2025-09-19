class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SimpleLinkedList:
    # constructor
    def __init__(self):
        self.head = None
        self.size = 0

    # ADD METHODS

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node
        self.size += 1

    # REMOVING METHODS
    def remove_first(self):
        if self.head is None:
            return False
        else:
            self.head = self.head.next
            self.size -= 1
            return True

    def remove_last(self):
        if self.head is None:
            return False
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
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

    def get_size(self):
        print(f'Existem {self.size} elementos na lista')

if __name__ == '__main__':
    elementos = SimpleLinkedList()

    elementos.add_first(1)
    elementos.add_last(2)
    elementos.add_last(3)

    elementos.remove_last()
    elementos.display()
    elementos.get_size()
