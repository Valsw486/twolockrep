class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Некоторый общий звук животного"

    def __str__(self):
        return f"{self.name}: {self.make_sound()}"


class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span  # размах крыльев в сантиметрах

    def make_sound(self):
        return "Чирик!"

    def __str__(self):
        return f"{self.name} (Птица, размах крыльев: {self.wing_span} см): {self.make_sound()}"


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color  # цвет шерсти

    def make_sound(self):
        return "Рев!"

    def __str__(self):
        return f"{self.name} (Млекопитающее, цвет шерсти: {self.fur_color}): {self.make_sound()}"


class Reptile(Animal):
    def __init__(self, name, scale_color):
        super().__init__(name)
        self.scale_color = scale_color  # цвет чешуи

    def make_sound(self):
        return "Шипение!"

    def __str__(self):
        return f"{self.name} (Рептилия, цвет чешуи: {self.scale_color}): {self.make_sound()}"


# Примеры использования
if __name__ == "__main__":
    попугай = Bird("Попугай", 25)
    лев = Mammal("Лев", "Золотистый")
    змея = Reptile("Змея", "Зеленый")

    print(попугай)
    print(лев)
    print(змея)