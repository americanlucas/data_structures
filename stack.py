class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.last_in = None
        self.size = 0

    # MÉTODOS

    # ADICIONA
    def push(self, value):
        new_item = Item(value)
        new_item.next = self.last_in
        self.last_in = new_item
        self.size += 1

    # REMOVE
    def pop(self):
        if self.last_in is None:
            return False
        else:
            self.last_in = self.last_in.next
            self.size -= 1
            return True

    # VERIFICA O ÚLTIMO INSERIDO
    def top(self):
        if self.last_in is None:
            print('You Must Have At Least One Element On The Stack')
            return
        current = self.last_in.value

        print(f'The Element On The Top Is {current}')

    # VERIFICA SE ESTÁ VAZIO
    def is_empty(self):
        if self.last_in is None:
            print('Stack IS EMPTY')
        else:
            print(f'You Still Have {self.size} Elements In The Stack')

    # LIMPA TODA A PILHA
    def clear(self):
        if self.last_in is None:
            print('Stack Is Already Empty')
        else:
            while self.last_in is not None:
                self.last_in = self.last_in.next
                self.size -= 1
            if self.last_in is None:
                print('You have Emptied The Stack')

if __name__ == "__main__":
    elementos = Stack()

    elementos.push(1)
    elementos.push(2)
    elementos.push(3)
    elementos.push(8)

    elementos.pop()
    elementos.pop()

    elementos.top()
    elementos.is_empty()
    elementos.clear()
