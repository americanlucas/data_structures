class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None   # INÍCIO DA FILA (ONDE OS ELEMENTOS IRÃO SAIR)
        self.back = None   # FINAL DA FILA (ONDE OS ELEMENTOS IRÃO ENTRAR)
        self.size = 0

    # MÉTODOS
    # ENFILEIRAR
    def enqueue(self, value):
        new_item = Item(value)
        if self.back is None:
            self.front = new_item      # front FICA FIXO
            self.back = new_item
        else:
            self.back.next = new_item  # INSERE O NOVO ITEM
            self.back = new_item       # TRANSFERE O FINAL DA FILA PARA O NOVO ITEM
        self.size += 1

    # DESENFILEIRAR
    def dequeue(self):
        if self.front is None:
            print('The Queue Is Empty')
            return False
        else:
            self.front = self.front.next
            self.size -= 1
            return  True

    # VERIFICA O PRIMEIRO DA FILA
    def top(self):
        if self.front is None:
            print('You Must Have At Least One Element On The Queue')
            return
        current = self.front.value

        print(f'The Element On The Top of the Queue Is {current}')

    # VERIFICA SE ESTÁ VAZIO
    def is_empty(self):
        if self.front is None:
            print('Queue IS EMPTY')
        else:
            print(f'You Still Have {self.size} Elements In The Queue')

    # LIMPA TODA A PILHA
    def clear(self):
        if self.front is None:
            print('Queue Is Already Empty')
        else:
            while self.front is not None:
                self.front = self.front.next
                self.size -= 1
            if self.front is None:
                print('You have Emptied The Queue')

if __name__ == '__main__':
    elementos = Queue()

    elementos.enqueue(2)
    elementos.enqueue(6)
    elementos.enqueue(4)
    elementos.enqueue(8)

    elementos.dequeue()

    elementos.top()
    elementos.clear()
    elementos.is_empty()
