# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def cat(self):
#         print(f"{self.name} ест")
#
#
# class Dog(Animal):
#     def dark(self):
#         print(f"{self.name} говорит: гав!")
#
#
# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} Говорит: мяу")
#
#
# dog = Dog("Бобик")
# cat = Cat("Мурзик")
#
# dog.dark()
# cat.meow()
#
# print()
#
# cat.eat()
# cat.meow()

class  Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def driv(self):
        print(f"{self.brand} едет в помощь")

class Tayota(Vehicle):

    def driv(self):
            print(f"{self.brand} - это Tayota")

class Honda(Tayota):
    def honda (self):
            print(f"{self.brand} машина сломалась")

tayota = Tayota("Tayota")
honda = Honda("Honda")

print()

tayota.driv()
tayota.driv()
honda.honda()
