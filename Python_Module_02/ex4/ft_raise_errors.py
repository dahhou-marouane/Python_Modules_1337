#!/usr/bin/env python3
def check_plant_health(
         plant_name: str,
         water_level: int,
         sunlight_hours: int
         ) -> str:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    try:
        water_level = int(water_level)
    except (TypeError, ValueError):
        raise ValueError(
                         f"Error: Water level '{water_level}' "
                         "is not a valid number"
                         )
    if water_level < 1:
        raise ValueError(
                         f"Error: Water level {water_level} "
                         "is too low (min 1)"
                         )
    elif water_level > 10:
        raise ValueError(
                         f"Error: Water level {water_level} "
                         "is too high (max 10)"
                         )
    try:
        sunlight_hours = int(sunlight_hours)
    except (TypeError, ValueError):
        raise ValueError(
                         f"Error: Sunlight hours '{sunlight_hours}' "
                         "is not a valid number"
                         )
    if sunlight_hours < 2:
        raise ValueError(
                         f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)"
                         )
    elif sunlight_hours > 12:
        raise ValueError(
                         f"Error: Sunlight hours {sunlight_hours} is "
                         "too high (max 12)"
                         )
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    plant_name = "tomato"
    water_level = 15
    sunlight_hours = 0

    try:
        print("Testing good values...")
        print(check_plant_health(plant_name, 5, 5))
    except Exception as e:
        print(e)
    try:
        print("\nTesting empty plant name...")
        print(check_plant_health("", 0, 0))
    except Exception as e:
        print(e)
    try:
        print("\nTesting bad water level...")
        print(check_plant_health(plant_name, water_level, sunlight_hours))
        print(f"Water level {water_level} is good", end="\n\n")
    except Exception as e:
        print(e)
    water_level = 8
    try:
        print("\nTesting bad sunlight hours...")
        print(check_plant_health(plant_name, water_level, sunlight_hours))
        print(f"Sunlight hours {sunlight_hours} is good")
    except Exception as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    try:
        test_plant_checks()
    except Exception as e:
        print(e)
