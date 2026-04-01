#!/usr/bin/env python3
def test_watering_system() -> None:
    plants_valid = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    plants_bad = [
        "tomato",
        "lettuce"
    ]
    try:
        print("=== Garden Watering System ===\n")
        print("Testing normal watering...")
        water_plants(plants_valid)
        print("\nTesting with error...")
        water_plants(plants_bad)
    except Exception as e:
        print(e)
    print("\nCleanup always happens, even with errors!")


def water_plants(plant_list: list[str]) -> None:
    if plant_list.__class__ is not list:
        print(f"Error: Plant list cannot be '{plant_list}'")
        return
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant.__class__ is not str:
                raise ValueError(f"Error: Cannot water {plant} - "
                                 "invalid plant!")
            if plant is None:
                raise ValueError(f"Error: Cannot water {plant} - "
                                 "invalid plant!")
            elif plant == "":
                raise ValueError(
                    "Error: Cannot water empty str - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        print(e)
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(e)
