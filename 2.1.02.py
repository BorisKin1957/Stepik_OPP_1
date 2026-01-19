'''Создайте класс TrafficLight, имитирующий светофор. Шаблон кода вызовет
все его методы по порядку.

Вам нужно:

    Создать класс TrafficLight.

    Определить в нем три метода:

        red_signal должен возвращать строку "Стоп".

        yellow_signal должен возвращать строку "Внимание".

        green_signal должен возвращать строку "Можно ехать".

Sample Input:

Sample Output:

Стоп
Внимание
Можно ехать

'''

class TrafficLight:
    def red_signal(myself):
        return 'Стоп'

    def yellow_signal(myself):
        return 'Внимание'

    def green_signal(myself):
        return 'Можно ехать'