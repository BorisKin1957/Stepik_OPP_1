'''Задача 5: Полный цикл (Геттер + Сеттер)
Условие:
Объединим все концепции в одном классе.

Вам нужно создать класс Thermostat:

В __init__ он принимает temp и сохраняет его в защищенный атрибут self._temperature.

Создайте геттер get_temperature().

Создайте сеттер set_temperature(new_temp), который позволяет устанавливать
температуру только в диапазоне от 0 до 100 градусов включительно.
Если new_temp выходит за этот диапазон, значение self._temperature меняться
не должно.'''


class Thermostat:
    def __init__(self, temp):
        self._temperature = temp

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, new_temp):
        if  isinstance(new_temp, (int, float)) and 0 <= new_temp <= 100:
            self._temperature = new_temp