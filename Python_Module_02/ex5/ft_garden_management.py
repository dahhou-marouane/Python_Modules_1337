#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    water_tank: int | str = 6

    def __init__(self) -> None:
        self.plants: list[tuple[str, int | str, int | str]] = []

    def set_water_tank(self, water: int | str) -> None:
        try:
            int(water)
        except (ValueError, TypeError):
            raise ValueError("Error: water tank should be int")
        GardenManager.water_tank = int(water)

    def add_plants(self,
                   plants: list[tuple[str, int | str, int | str]]
                   ) -> None:
        try:
            print("=== Garden Management System ===\n")
            print("Adding plants to garden...")
            if plants.__class__ is not list:
                raise PlantError(
                    "Error: The input plants should be 'list[tuple[str, int | "
                    "str, int | str]'")
            for plt in plants[:]:
                try:
                    if plt.__class__ is not tuple:
                        plants.remove(plt)
                        raise PlantError(
                            "Error: inside plant list should be "
                            "'tuple[str, int, int]'")
                    name, water_level, sunlight_hours = plt
                    if name == "":
                        raise PlantError(
                            "Error adding plant: Plant name cannot be empty!")
                    if name.__class__ is not str or not name:
                        plants.remove(plt)
                        raise PlantError(
                            f"Error adding plant: Plant name cannot be "
                            f"{name.__class__.__name__}!")
                    else:
                        plant: tuple[str, int | str, int | str] = (
                            name, water_level, sunlight_hours)
                        self.plants.append(plant)
                        print(f"Added {name} successfully")
                except PlantError as e:
                    print(e)
        except Exception as e:
            print(e)
        print()

    def water_plants(self) -> None:
        try:
            print("Watering plants...")
            print("Opening watering system")
            for plt in self.plants[:]:
                try:
                    name, water_level, _ = plt
                    try:
                        water_level = int(water_level)
                    except (ValueError, TypeError):
                        self.plants.remove(plt)
                        raise WaterError(
                            f"Error: water_level of plant {name} "
                            "should be int")
                    if int(self.water_tank) >= 3:
                        print(f"Watering {name} - success")
                        self.water_tank = int(self.water_tank) - 3
                    else:
                        print(
                            f"Error watering {name}: Not enough water in tank")
                except GardenError as e:
                    print(e)
        except Exception as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")
        print()

    def check_plant_health(self) -> None:
        try:
            print("Checking plant health...")
            for plt in self.plants:
                try:
                    name, water_level, sun = plt
                    try:
                        sun = int(sun)
                        water_level = int(water_level)
                    except ValueError:
                        raise PlantError(
                            f"Error: sunlight hours of plant {name} should be"
                            " int")
                    if water_level < 1:
                        raise WaterError(
                            f"Error checking {name}: Water level {water_level}"
                            " is too low (min 1)")
                    elif water_level > 10:
                        raise WaterError(
                            f"Error checking {name}: Water level {water_level}"
                            " is too high (max 10)")
                    elif sun < 2:
                        raise PlantError(
                            f"Error checking {name}: sunlight hours "
                            f"{sun} is too low (min 2)")
                    elif sun > 12:
                        raise PlantError(
                            f"Error checking {name}: sunlight hours "
                            f"{sun} is too high (max 12)")
                    else:
                        print(f"{name}: healthy (water: {water_level}, "
                              f"sun: {sun})")
                except GardenError as e:
                    print(e)
        except Exception as e:
            print(e)
        print()

    def recovery(self) -> None:
        try:
            print("Testing error recovery...")
            if int(self.water_tank) < 3:
                raise GardenError("Not enough water in tank")
            print("enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        print("System recovered and continuing...\n")
        print("Garden management system test complete!")


def test_garden_management() -> None:
    manager = GardenManager()
    plants: list[tuple[str, int | str, int | str]] = [
        ("tomato", "5", "8"),
        ("lettuce", 15, 5),
        ("", 5, 6)
    ]
    water: int | str = 6
    if plants.__class__ is not list:
        raise ValueError("Plants should be list")
    manager.set_water_tank(water)
    manager.add_plants(plants)
    manager.water_plants()
    manager.check_plant_health()
    manager.recovery()


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print(e)
