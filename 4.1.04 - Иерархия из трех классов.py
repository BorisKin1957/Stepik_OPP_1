'''Задача 4: Иерархия из трех классов
Условие:
Наследование можно выстраивать в длинные цепочки.

Вам нужно создать иерархию классов: Shape -> Polygon -> Square.

Shape: __init__ принимает color. Имеет метод get_color(), возвращающий цвет.

Polygon: Наследует от Shape. Его __init__ принимает color и num_sides (число сторон).
Используйте super() для цвета.

Square: Наследует от Polygon. Его __init__ принимает color и side_length (длина стороны).
Он должен вызвать super().__init__() для родителя, передав ему color и то,
что у квадрата всегда 4 стороны.'''

'''Задача 4: Иерархия из трех классов
Условие:
Наследование можно выстраивать в длинные цепочки.

Вам нужно создать иерархию классов: Shape -> Polygon -> Square.

Shape: __init__ принимает color. Имеет метод get_color(), возвращающий цвет.

Polygon: Наследует от Shape. Его __init__ принимает color и num_sides (число сторон). 
Используйте super() для цвета.

Square: Наследует от Polygon. Его __init__ принимает color и side_length (длина стороны). 
Он должен вызвать super().__init__() для родителя, передав ему color и то, 
что у квадрата всегда 4 стороны.'''

class Shape:
    def __init__(self, color):
        self.color = color  # Сохраняем цвет фигуры

    def get_color(self):
        return self.color  # Возвращаем цвет

class Polygon(Shape):
    def __init__(self, color, num_sides):
        super().__init__(color)  # Инициализируем родительский класс Shape
        self.num_sides = num_sides  # Устанавливаем количество сторон

class Square(Polygon):
    def __init__(self, color, side_length):
        super().__init__(color, 4)  # Вызываем __init__ у Polygon: цвет и 4 стороны
        self.side_length = side_length  # Добавляем длину стороны квадрата

# Исправление ошибки:
# В исходном коде: super().__init__(color) — это вызывает Shape.__init__, но не передаёт num_sides в Polygon.
# Правильно: вызывать super().__init__(color, 4), чтобы инициализировать Polygon полностью.
# Также не нужно вручную присваивать self.num_sides = 4 — это уже делает Polygon при вызове super().
# Но если хочется явно подчеркнуть, что num_sides = 4, можно оставить, но лучше полагаться на родительский класс.

