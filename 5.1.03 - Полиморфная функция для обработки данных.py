'''
Задача 3: Полиморфная функция для обработки данных

Условие:
Напишите единую функцию, которая может работать с разными источниками
данных благодаря полиморфизму.

Вам нужно:

    Создать два класса: StringSource и ListSource.

    В StringSource.__init__ принимать строку и сохранять ее.
    В ListSource.__init__ принимать список и сохранять его.

    В обоих классах определить метод get_length(), который возвращает количество
    элементов в источнике (для строки — количество символов, для списка —
    количество элементов). Используйте len().

    Написать полиморфную функцию print_source_length(source), которая принимает
     любой из этих объектов и печатает строку "Длина источника: [длина]".
'''

class StringSource:
    def __init__(self, source):
        # Проверяем, что переданная source — это строка
        if isinstance(source, str):
            self.source = source
        else:
            raise TypeError("StringSource ожидает строку")

    def get_length(self):
        # Возвращает длину строки
        return len(self.source)


class ListSource:
    def __init__(self, source):
        # Проверяем, что переданная source — это список
        if isinstance(source, list):
            self.source = source
        else:
            raise TypeError("ListSource ожидает список")

    def get_length(self):
        # Возвращает длину списка
        return len(self.source)


def print_source_length(source):
    # Полиморфная функция: работает с любым объектом, имеющим метод get_length()
    print(f'Длина источника: {source.get_length()}')


# Пример вызова кода
if __name__ == "__main__":
    # Создаём экземпляр для строки
    string_data = StringSource("Привет, мир!")
    print_source_length(string_data)  # Длина источника: 12

    # Создаём экземпляр для списка
    list_data = ListSource([1, 2, 3, 4, 5])
    print_source_length(list_data)  # Длина источника: 5

'''Объяснение:

Классы StringSource и ListSource реализуют один и тот же метод get_length(), 
что позволяет использовать их полиморфно.
Функция print_source_length() не зависит от конкретного типа — она работает 
с любым объектом, у которого есть метод get_length().
Добавлены проверки типов в конструкторах и выброс исключений при неверных 
данных.
В конце добавлен пример использования с двумя типами данных.'''

