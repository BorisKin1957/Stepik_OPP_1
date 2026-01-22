'''Задача 3: Геттер
Условие:
Создайте "официальный" способ для чтения защищенных данных.

Вам нужно:

Создать класс Secret.

В __init__ принять secret_message и сохранить его в защищенный атрибут self._message.

Создать публичный метод-геттер get_message(), который возвращает значение self._message.'''


class Secret():
    def __init__(self, secret_message):
        self._message = secret_message

    def get_message(self):
        return self._message