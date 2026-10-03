class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        print(f"Привет я  {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает")
        self.health += 1


hero1 = Hero("Аман", 10, 100, 100)
hero1.greet()
hero1.attack()
hero1.rest()

print(hero1.strength, hero1.health)

hero2 = Hero("Артур", 15, 200, 1700)
hero2.greet()
hero2.attack()
hero2.rest()

print(hero2.strength, hero2.health)



