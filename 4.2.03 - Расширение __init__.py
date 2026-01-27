'''
Задача 3: Расширение __init__

Условие:
Самый частый случай использования super() — расширение конструктора.

Вам нужно:

    Создать родительский класс Product с __init__, который принимает name и price.

    Создать дочерний класс DiscountedProduct, который наследует от Product.

    DiscountedProduct.__init__ должен принимать name, price и discount.

    Внутри DiscountedProduct.__init__ нужно:

        Вызвать родительский __init__ с помощью super(), чтобы сохранить name и price.

        Создать новый атрибут экземпляра self.discount.
'''


'''
Задача 3: Расширение __init__

Условие:
Самый частый случай использования super() — расширение конструктора.

Вам нужно:

    Создать родительский класс Product с __init__, который принимает name и price.

    Создать дочерний класс DiscountedProduct, который наследует от Product.

    DiscountedProduct.__init__ должен принимать name, price и discount.

    Внутри DiscountedProduct.__init__ нужно:

        Вызвать родительский __init__ с помощью super(), чтобы сохранить name и price.

        Создать новый атрибут экземпляра self.discount.
'''

# Определение родительского класса Product
class Product:
    # Конструктор класса Product, принимает два параметра: name (название) и price (цена)
    def __init__(self, name, price):
        # Сохраняем переданное имя как атрибут экземпляра
        self.name = name
        # Сохраняем переданную цену как атрибут экземпляра
        self.price = price

# Определение дочернего класса DiscountedProduct, который наследуется от Product
class DiscountedProduct(Product):
    # Конструктор класса DiscountedProduct, принимает три параметра: name, price и discount
    def __init__(self, name, price, discount):
        # Вызываем конструктор родительского класса Product с помощью super(),
        # чтобы инициализировать атрибуты name и price
        super().__init__(name, price)
        # Добавляем новый атрибут экземпляра — размер скидки (в долях единицы или процентах)
        self.discount = discount