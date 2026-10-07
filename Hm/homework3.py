#
# from abc import ABC, abstractmethod
#
#
# class Hero(ABC):
#     def __init__(self, name, level, health, strength):
#         self.name = name
#         self.level = level
#         self.__health = health
#         self.strength = strength
#
#     def greet(self):
#         print(f"Привет, я {self.name}, мой уровень {self.level}")
#
#     def rest(self):
#         print(f"{self.name} отдыхает")
#         self.__health += 1
#
#     @abstractmethod
#     def attack(self):
#         pass
#
#
# class Warrior(Hero):
#     def attack(self):
#         print(f"{self.name} атакует мечом")
#
#
# class Mage(Hero):
#     def attack(self):
#         print(f"{self.name} использует магию")
#
#
# class Assassin(Hero):
#     def attack(self):
#         print(f"{self.name} атакует из-под тишка")
#
#
# hero1 = Warrior("Кратос", 10, 100, 50)
# hero2 = Mage("Мерлин", 15, 80, 70)
# hero3 = Assassin("Тень", 20, 90, 60)
#
#
# hero1.greet()
# hero1.attack()
# hero1.rest()
#
# print()
#
# hero2.greet()
# hero2.attack()
# hero2.rest()
#
# print()
#
# hero3.greet()
# hero3.attack()
# hero3.rest()
from multiprocessing.spawn import set_executable

from Hm.homework1 import Hero


# from encodings.punycode import selective_find


# class Hero:
#     def __init__(self, name, level, health, strength):
#         self.name = name
#         self.level = level
#         self.health = health
#         self.strength = strength
#
#     def greet(self):
#         print(f"Привет, я {self.name}, мой уровень {self.level}")
#
#     def attack(self):
#         print(f"{self.name} наносит удар!")
#         self.strength -= 1
#
#     def rest(self):
#         print(f"{self.name} отдыхает...")
#         self.health += 1
#
#
# # Создаем первого героя
# hero1 = Hero("Аман", 5, 100, 20)
#
# # Создаем второго героя
# hero2 = Hero("Артур", 10, 80, 15)
#
#
# # Первый герой
# print("=== Первый герой ===")
# hero1.greet()
#
# print("Здоровье до отдыха:", hero1.health)
# hero1.rest()
# print("Здоровье после отдыха:", hero1.health)
#
# print("Сила до атаки:", hero1.strength)
# hero1.attack()
# print("Сила после атаки:", hero1.strength)
#
#
# # Второй герой
# print("\n=== Второй герой ===")
# hero2.greet()
#
# print("Здоровье до отдыха:", hero2.health)
# hero2.rest()
# print("Здоровье после отдыха:", hero2.health)
#
# print("Сила до атаки:", hero2.strength)
# hero2.attack()
# print("Сила после атаки:", hero2.strength)

# class Hero:
#     def __init__(self, name, level, strength, health):
#         self.name = name
#         self.strength = strength
#         self.level = level
#         self.health = health
#
#     def greet (self):
#         print(f" Привет я {self.name}, мой уровень {self.level} ")
#
#     def attack(self):
#         print(f"{self.name}, наносит удар")
#         self.strength -= 1
#     def rest(self):
#         print(f"{self.health} отдыхает ...")
#         self.health += 1
#
#     #Создаем первого игрока
#     hero1 = Hero ("Ferdinant", 10, 170, 200)
#
#     #Второй игрок
#     hero2 = Hero ("Madara", 70, 800, 300)
#
#     #Первый игрок
#     print("=== Первый игрок === ")
#     hero1.greet()
#
#     print("Здоровье до отдыха:", hero1.health)
#     hero1.rest()
#     print("Здоровье после отдыха:", hero1.health)
#
#     print("Сила до удара", hero1.strength)
#     hero1.attack()
#     print("Сила после удара:", hero1.strength)
#
#     #Второй игрок
#     print("=== Второй игрок ===")
#     hero2.greet()
#
#     print("Здоровье до отдыха")
#     hero2.rest()
#     print("Здоровье после отдыха")
#
#     print("Сила после удара")
#     hero2.attack()
#     print("СИла после удара")

class Animal:
      def __init__(self, name):
        self.name = name

      def cat(self):
       print(f"{self.name} ест")

class Dog(Animal):
      def dark (self):
            print(f"{self.name} говорит: гав!")

class Cat(Animal):
      def meow (self):
            print(f"{self.name} Говорит: мяу")

dog = Dog("Бобик")
cat = Cat("Мурзик")

dog.dark()
cat.meow()

print()

cat.eat()
cat.meow()


