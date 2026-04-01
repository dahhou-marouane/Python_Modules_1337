#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water(water: int) -> None:
    try:
        tank_water = int(water)
    except (TypeError, ValueError):
        raise WaterError("input tank water is not int")
    if tank_water > 3:
        print("Enough water in the tank")
        return
    else:
        raise WaterError("Not enough water in the tank!")


def plant_wilting(water: int) -> None:
    try:
        water_level = int(water)
    except (TypeError, ValueError):
        raise PlantError("input water is not int")
    if water_level > 3:
        print("The tomato plant is good")
        return
    else:
        raise PlantError("The tomato plant is wilting!")


def custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    input = 0
    print("Testing PlantError...")
    try:
        plant_wilting(input)
        print()
    except PlantError as e:

        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        water(input)
        print()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for test in (plant_wilting, water):
        try:
            test(input)
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    try:
        custom_errors()
    except Exception as e:
        print(e)
