'''
Задача 2: Простое использование issubclass()

Условие:
Теперь давайте поработаем с классами, а не с объектами.

Вам нужно:

    Создать три класса: Vehicle, Car(Vehicle) и Boat(Vehicle).

    Написать отдельную функцию is_land_vehicle(vehicle_class), которая:

        Принимает на вход один класс vehicle_class.

        Возвращает True, если vehicle_class является подклассом Car.

        Возвращает False в остальных случаях.

        Используйте issubclass() для проверки.
'''

'''
Задача 2: Простое использование issubclass()

Условие:
Теперь давайте поработаем с классами, а не с объектами.

Вам нужно:

    Создать три класса: Vehicle, Car(Vehicle) и Boat(Vehicle).

    Написать отдельную функцию is_land_vehicle(vehicle_class), которая:

        Принимает на вход один класс vehicle_class.

        Возвращает True, если vehicle_class является подклассом Car.

        Возвращает False в остальных случаях.

        Используйте issubclass() для проверки.
'''

# Базовый класс для всех транспортных средств
class Vehicle:
    pass

# Класс Car, наследующийся от Vehicle — представляет наземное транспортное средство
class Car(Vehicle):
    pass

# Класс Boat, наследующийся от Vehicle — представляет водное транспортное средство
class Boat(Vehicle):
    pass


# Функция проверяет, является ли переданный класс подклассом Car
def is_land_vehicle(vehicle_class):
    # Возвращает True, если vehicle_class — это подкласс Car (включая сам класс Car)
    return issubclass(vehicle_class, Car)

print(is_land_vehicle(Car))
print(is_land_vehicle(Boat))
print(is_land_vehicle(Vehicle))

'''Пояснение:

issubclass(A, B) возвращает True, если класс A является наследником класса 
B или совпадает с ним.
В данном случае is_land_vehicle(Car) вернёт True, потому что Car считается 
подклассом самого себя.
is_land_vehicle(Boat) вернёт False, так как Boat не наследуется от Car.
is_land_vehicle(Vehicle) тоже вернёт False, потому что Vehicle — родительский 
класс, а не дочерний для Car.'''