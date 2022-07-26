# coding: utf-8
'''
На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации
'''
class first_way():
    def __init__(self):
        self._fifo = []

    def get(self,):
        try:
            return self._fifo.pop(0)
        except IndexError:
            return None

    def set(self, value):
        self._fifo.append(value)



from collections import deque
class second_way():
    def __init__(self):
        self._fifo_que = deque()

    def get(self):
        try:
            return self._fifo_que.popleft()
        except IndexError:
            return None

    def set(self, value):
        self._fifo_que.append(value)



'''
Первый класс реализован через список его минус в медленной скорости, так как питон сначала при операции pop смещает каждый элемент влево,
отсюда скорость O(n).

Второй способ реализован через стандартную библиотеку питона deque, которая хранит два связанных списка в одном, что позволят очень быстро 
извлекать и добовлять элементы в концы списка, но если попытаться добавить в центр списка значение, это будет значительно дольше. 
Скорость данного способа при использовании его как очередь fifo O(1).


p.s. Не использовал магические методы, так как __setattr__ работает нормально, а вот __getattr__ работает только при вызове несуществующего
значения, и может приводить к бесконечной рекурсии  в версии 2.7

p.s.s 
Ниже под комментарием реализована проверка работы программы
'''

class worker():
    first = first_way()
    second = second_way()

work = worker()
work.first.set('one')
work.first.set('two')
work.second.set('one')
work.second.set('two')


print work.first.get()
print work.first.get()
print work.first.get()

print work.second.get()
print work.second.get()
print work.second.get()
