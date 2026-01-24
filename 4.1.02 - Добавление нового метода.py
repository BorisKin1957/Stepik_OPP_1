'''Задача 2: Добавление нового метода
Условие:
Дочерний класс может не только наследовать, но и добавлять свои, уникальные методы.

Вам нужно:

Создать родительский класс Publication (Публикация) с __init__, который принимает
title и сохраняет его.

Создать дочерний класс Book, который наследует от Publication.

В классе Book добавить новый метод get_author(author_name), который возвращает
строку в формате "Автор книги '[title]' - [author_name]". Этот метод должен
использовать унаследованный атрибут self.title.'''

class Publication:
    def __init__(self, title):
        self.title = title


class Book(Publication):
    def get_author(self, author_name):
        return f"Автор книги '{self.title}' - {author_name}"

'''Объяснение:

Класс Publication инициализирует атрибут title.
Класс Book наследуется от Publication и получает доступ к атрибуту self.title.
В Book добавлен метод get_author, который использует self.title и принимает имя 
автора, возвращая отформатированную строку.'''
