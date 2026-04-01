#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = self.set_height(height)
        self._age = self.set_age(age)

    def set_height(self, height: int) -> int:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return 0
        else:
            print(f"Height updated: {height}cm [OK]")
            return height

    def set_age(self, age: int) -> int:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return 0
        else:
            print(f"Age updated: {age} days [OK]")
            return age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    name = "Rose"
    print(f"Plant created: {name}")
    plant = SecurePlant(name, 25, 30)
    print()
    if plant.set_height(-5):
        plant.set_age(25)
    print(f"\nCurrent plant: {plant.name} "
          f"({plant.get_height()}cm, {plant.get_age()} days)")
