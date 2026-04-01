#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def get_name(self) -> str:
        return self.name


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_color(self) -> str:
        return self.color

    def get_info(self) -> None:
        print(f"{self.get_name()} ({self.__class__.__name__}): "
              f"{self.get_height()}cm, {self.get_age()} days, "
              f"{self.get_color()} color"
              )


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        my_calc = self.height * 3.14 * self.trunk_diameter / 1000

        print(f"{self.name} provides "
              f"{my_calc:.0f} "
              "square meters of shade"
              )

    def get_trunk_diameter(self) -> int:
        return self.trunk_diameter

    def get_info(self) -> None:
        print(f"{self.get_name()} ({self.__class__.__name__}): "
              f"{self.get_height()}cm, {self.get_age()} days, "
              f"{self.get_trunk_diameter()}cm diameter"
              )


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest_nutritional(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def get_nutritional_value(self) -> str:
        return self.nutritional_value

    def get_harvest_season(self) -> str:
        return self.harvest_season

    def get_info(self) -> None:
        print(f"{self.get_name()} ({self.__class__.__name__}): "
              f"{self.get_height()}cm, {self.get_age()} days, "
              f"{self.get_harvest_season()} harvest"
              )


if __name__ == "__main__":
    flower = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 80, 45, "yellow"),
        Flower("Tulip", 25, 30, "red")
        ]
    tree = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 900, 3650, 80),
        Tree("Maple", 700, 2920, 60)
        ]
    vegetable = [
        Vegetable("Tomato", 80, 90, "summer", "C"),
        Vegetable("Carrot", 30, 70, "winter", "A"),
        Vegetable("Potato", 60, 120, "autumn", "C")
        ]
    print("=== Garden Plant Types ===", end="\n\n")
    for flowers in flower:
        flowers.get_info()
        flowers.bloom()
        print()
    print()
    for trees in tree:
        trees.get_info()
        trees.produce_shade()
        print()
    print()
    for vegetables in vegetable:
        vegetables.get_info()
        vegetables.harvest_nutritional()
        print()
