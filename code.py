class TwoStacksQueue:
    def __init__(self):
        self.stack_push = [] # стек для добавления новых элементов
        self.stack_pop = [] # стек для извлечения элементов

    # Добавить элемент в конец очереди
    def enqueue(self, x):
        self.stack_push.append(x)   # просто кладём в первый стек

    # Удалить и вернуть первый (самый старый) элемент очереди
    def dequeue(self):
        # Если оба стека пусты, очередь пуста — возвращаем None
        if not self.stack_push and not self.stack_pop:
            return None
        # Если стек извлечения пуст, перекладываем всё из стека добавления
        if not self.stack_pop:
            while self.stack_push:
                # Берём верхний из push и кладём в pop (тем самым переворачиваем порядок)
                self.stack_pop.append(self.stack_push.pop())
        # Теперь на вершине stack_pop лежит первый элемент очереди — забираем его
        return self.stack_pop.pop()

    # Посмотреть первый элемент очереди, не удаляя его
    def front(self):
        # Если оба стека пусты — очередь пуста
        if not self.stack_push and not self.stack_pop:
            return None
        # Если pop-стек пуст, перекладываем из push-стека
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        # Возвращаем верхний элемент pop-стека (без удаления)
        return self.stack_pop[-1]

# Проверка работы
q = TwoStacksQueue(3)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q.front()) # A
q.enqueue('D') # Перезаписывает A
print(q.dequeue()) # B
print(q.dequeue()) # C
print(q.dequeue()) # D
