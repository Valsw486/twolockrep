import pickle
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.__class__.__name__} {self.name}, Age: {self.age}'
class ZooKeeper(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
    def feed_animal(self, animal_name):
        print(f"{self.name} is feeding the animal: {animal_name}")
class Veterinarian(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
    def heal_animal(self, animal_name):
        print(f"{self.name} is healing the animal: {animal_name}")
class Zoo:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.employees, file)
        print("Zoo information saved.")
    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.employees = pickle.load(file)
            print("Zoo information loaded.")
        except FileNotFoundError:
            print("File not found. Starting with an empty zoo.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def show_employees(self):
        for employee in self.employees:
            print(employee)
# Пример использования классов
if __name__ == "__main__":
    zoo = Zoo()
    # Загружаем информацию о зоопарке, если файл существует
    zoo.load_from_file("zoo_data.pkl")
    # Добавляем сотрудников
    zookeeper = ZooKeeper("John", 30)
    veterinarian = Veterinarian("Dr. Smith", 45)
    zoo.add_employee(zookeeper)
    zoo.add_employee(veterinarian)
    # Показываем сотрудников
    zoo.show_employees()
    # Сохраняем информацию о зоопарке в файл
    zoo.save_to_file("zoo_data.pkl")
