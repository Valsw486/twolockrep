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
# Пример использования классов
if __name__ == "__main__":
    zookeeper = ZooKeeper("John", 30)
    veterinarian = Veterinarian("Dr. Smith", 45)
    print(zookeeper)
    zookeeper.feed_animal("Lion")
    print(veterinarian)
    veterinarian.heal_animal("Tiger")
