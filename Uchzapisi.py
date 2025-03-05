class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id           # Уникальный идентификатор
        self.__name = name                 # Имя пользователя
        self.__access_level = 'user'       # Уровень доступа

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'      # Уровень доступа для администраторов
        self.__users = []                   # Список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Можно добавлять только объекты класса User.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь не найден.")

    def list_users(self):
        if not self.__users:
            print("Нет пользователей в системе.")
        else:
            print("Список пользователей:")
            for user in self.__users:
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


# Пример использования

# Создаем администраторов и пользователей
admin = Admin(user_id=1, name="Admin1")
user1 = User(user_id=2, name="User1")
user2 = User(user_id=3, name="User2")

# Добавляем пользователей через администратора
admin.add_user(user1)
admin.add_user(user2)

# Список пользователей
admin.list_users()

# Удаляем пользователя
admin.remove_user(user_id=2)

# Список пользователей после удаления
admin.list_users()
