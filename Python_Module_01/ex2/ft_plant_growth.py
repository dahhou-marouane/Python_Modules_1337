#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.Age = age

    def grow(self) -> None:
        self.height = self.height + 1

    def age(self) -> None:
        self.Age = self.Age + 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
        ]
    day = 1
    height = plants[0].height
    print(f"=== Day {day} ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.Age} days old")
    for plant in plants:
        day = 1
        for i in range(1, 7):
            plant.age()
            plant.grow()
            day += 1
    print(f"=== Day {day} ===")
    for plant in plants:
        plant.get_info()
    print(f'Growth this week: +{plants[0].height - height}cm')
