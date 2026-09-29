class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


# Создаем первого героя
hero1 = Hero("Аман", 5, 100, 20)

# Создаем второго героя
hero2 = Hero("Артур", 10, 80, 15)


# Первый герой
print("=== Первый герой ===")
hero1.greet()

print("Здоровье до отдыха:", hero1.health)
hero1.rest()
print("Здоровье после отдыха:", hero1.health)

print("Сила до атаки:", hero1.strength)
hero1.attack()
print("Сила после атаки:", hero1.strength)


# Второй герой
print("\n=== Второй герой ===")
hero2.greet()

print("Здоровье до отдыха:", hero2.health)
hero2.rest()
print("Здоровье после отдыха:", hero2.health)

print("Сила до атаки:", hero2.strength)
hero2.attack()
print("Сила после атаки:", hero2.strength)