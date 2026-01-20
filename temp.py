class Book:
    def __init__(self, title, author, year):
        # Получаем аргументы и сохраняем их как атрибуты
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True # Атрибут по умолчанию

    def show_info(self):
        status = "в наличии" if self.is_available else "выдана"
        print(f'"{self.title}", {self.author} ({self.year} г.) - Статус: {status}')

# Создаем первый объект-книгу
book_1 = Book("Хоббит, или Туда и обратно", "Дж. Р. Р. Толкин", 1937)

# Создаем второй, совершенно другой объект
book_2 = Book("1984", "Джордж Оруэлл", 1949)

book_1.show_info()
#book_2.is_available = False
book_2.show_info()