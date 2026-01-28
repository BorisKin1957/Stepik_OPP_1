'''
Задача 5: isinstance и унаследованные атрибуты

Условие:
Объединим isinstance с работой с атрибутами.

Вам нужно:

    Создать классы User и Admin(User).

    В User.__init__ принимать username и сохранять его.

    В Admin.__init__ принимать username и access_level, используя super() для username.

    Написать полиморфную функцию get_user_description(user_object), которая:

        Принимает на вход объект user_object.

        Если объект является экземпляром Admin, возвращает строку
        "Администратор [username] с уровнем доступа [access_level]".

        Если объект является экземпляром User (но не Admin), возвращает строку
        "Пользователь [username]".
'''

'''
Задача 5: isinstance и унаследованные атрибуты

Условие:
Объединим isinstance с работой с атрибутами.

Вам нужно:

    Создать классы User и Admin(User).

    В User.__init__ принимать username и сохранять его.

    В Admin.__init__ принимать username и access_level, используя super() для username.

    Написать полиморфную функцию get_user_description(user_object), которая:

        Принимает на вход объект user_object.

        Если объект является экземпляром Admin, возвращает строку
        "Администратор [username] с уровнем доступа [access_level]".

        Если объект является экземпляром User (но не Admin), возвращает строку
        "Пользователь [username]".
'''

# Определяем базовый класс User
class User:
    # Конструктор класса User, принимает имя пользователя
    def __init__(self, username):
        # Сохраняем переданное имя пользователя как атрибут экземпляра
        self.username = username

    # Метод для получения имени пользователя
    def get_username(self):
        # Возвращает значение атрибута username
        return self.username


# Определяем класс Admin, который наследуется от User
class Admin(User):
    # Конструктор класса Admin, принимает имя пользователя и уровень доступа
    def __init__(self, username, access_level):
        # Вызываем конструктор родительского класса User, чтобы установить username
        super().__init__(username)
        # Добавляем дополнительный атрибут — уровень доступа
        self.access_level = access_level

    # Метод для получения уровня доступа
    def get_access_level(self):
        # Возвращает значение атрибута access_level
        return self.access_level


# Полиморфная функция для получения описания пользователя
def get_user_description(user_object):
    # Проверяем, является ли объект экземпляром класса Admin
    if isinstance(user_object, Admin):
        # Формируем и возвращаем строку с информацией об администраторе
        return (f'Администратор {user_object.get_username()} с уровнем доступа '
                f'{user_object.get_access_level()}')
    # Если объект — экземпляр User (и не Admin, так как Admin уже был проверен выше)
    elif isinstance(user_object, User):
        # Возвращаем строку с информацией о пользователе
        return f'Пользователь {user_object.get_username()}'


'''Пояснение:

Использование isinstance() позволяет корректно определить тип объекта, 
учитывая иерархию наследования.
Так как Admin наследуется от User, все экземпляры Admin также являются экземплярами 
User, но порядок проверки важен: сначала проверяется Admin, потом User, чтобы 
избежать ложного срабатывания.
Методы get_username() и get_access_level() обеспечивают инкапсуляцию — 
доступ к данным через интерфейс, а не напрямую к атрибутам (хотя в Python это 
скорее соглашение).
Если хотите, могу предложить версию с прямым доступом к атрибутам или 
с аннотацией типов.'''