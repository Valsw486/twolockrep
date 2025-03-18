class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):
        """Метод, который будет переопределен в подклассах."""
        raise NotImplementedError("Этот метод нужно переопределить в подклассе")

    def eat(self, food):
        """Метод, который выводит информацию о том, что животное ест."""
        print(f"{self.name} ест {food}.")

# Пример подкласса для конкретного животного
class Dog(Animal):
    def make_sound(self):
        return "Гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

# Пример использования
my_dog = Dog("Бобик", 3)
my_cat = Cat("Мурка", 2)

print(f"{my_dog.name} говорит: {my_dog.make_sound()}")
my_dog.eat("корм")

print(f"{my_cat.name} говорит: {my_cat.make_sound()}")
my_cat.eat("рыбу")
