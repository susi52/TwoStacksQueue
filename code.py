class TwoStacksQueue:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.stack_push = [] # Стек для добавления новых элементов
        self.stack_pop = [] # Стек для извлечения элементов

    def enqueue(self, x):
        # Если максимальный размер задан и очередь уже заполнена
        if self.max_size is not None and (len(self.stack_push) + len(self.stack_pop)) == self.max_size:
            # Удаляем самый старый элемент (голову) – перезапись при переполнении
            self.dequeue()
        # Добавляем новый элемент в стек добавления
        self.stack_push.append(x)

    def dequeue(self):
        # Если оба стека пусты, очередь пуста 
        if not self.stack_push and not self.stack_pop:
            return None
        # Если стек извлечения пуст, перекладываем все элементы из стека добавления
        if not self.stack_pop:
            while self.stack_push:
                # Берём верхний из push и кладём в pop (порядок переворачивается)
                self.stack_pop.append(self.stack_push.pop())
        # Теперь на вершине stack_pop лежит первый элемент очереди – забираем его
        return self.stack_pop.pop()

    def front(self):
        # Если оба стека пусты – очередь пуста
        if not self.stack_push and not self.stack_pop:
            return None
        # Если стек извлечения пуст, перекладываем из стека добавления
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        # Возвращаем верхний элемент стека извлечения (без удаления)
        return self.stack_pop[-1]

# Проверка работы
q = TwoStacksQueue(3)      
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q.front()) # A 
q.enqueue('D') # переполнение, удаляется 'A', добавляется 'D'
print(q.dequeue()) # B
print(q.dequeue()) # C
print(q.dequeue()) # D
