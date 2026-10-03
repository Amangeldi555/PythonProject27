
from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом")


class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию")


class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка")


hero1 = Warrior("Кратос", 10, 100, 50)
hero2 = Mage("Мерлин", 15, 80, 70)
hero3 = Assassin("Тень", 20, 90, 60)


hero1.greet()
hero1.attack()
hero1.rest()

print()

hero2.greet()
hero2.attack()
hero2.rest()

print()

hero3.greet()
hero3.attack()
hero3.rest()