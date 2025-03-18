class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def make_sound(self):
        return "Гав!"
class Cat(Animal):
    def make_sound(self):
        return "мяу!"
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def __str__(self):
        return f"{self.name}, {self.role}"
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def add_employee(self, employee):
        self.employees.append(employee)
    def show_animals(self):
        for animal in self.animals:
            print(f"Animal: {animal.name}, Sound: {animal.make_sound()}")
    def show_employees(self):
        for employee in self.employees:
            print(f"Employee: {employee}")
# Пример использования
if __name__ == "__main__":
    zoo = Zoo()
    # Добавление животных
    dog = Dog("Жучка")
    cat = Cat("Мурка")
    zoo.add_animal(dog)
    zoo.add_animal(cat)
    # Добавление сотрудников
    employee1 = Employee("Маша", "Сторож")
    employee2 = Employee("Петя", "Ветеринар")
    zoo.add_employee(employee1)
    zoo.add_employee(employee2)
    # Показать животных и сотрудников
    print("Animals in the zoo:")
    zoo.show_animals()
    print("\nEmployees in the zoo:")
    zoo.show_employees()
