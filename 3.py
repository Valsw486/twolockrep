class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def make_sound(self):
        return "Гав!"
class Cat(Animal):
    def make_sound(self):
        return "Mяу!"
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())
# Пример использования
if __name__ == "__main__":
    animals = [Dog(), Cat()]
    animal_sound(animals)
