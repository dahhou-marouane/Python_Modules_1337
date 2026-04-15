#!/usr/bin/env python3
def check_temperature(temp_str: str) -> int:
    try:
        formatted = int(temp_str)
    except (TypeError, ValueError):
        raise ValueError(
            f"Error: '{temp_str}' is not a "
            "valid number")
    if formatted > 40:
        raise ValueError(
            f"Error: {formatted}°C is too hot "
            "for plants (max 40°C)")
    if formatted < 0:
        raise ValueError(
            f"Error: {formatted}°C is too cold "
            "for plants (min 0°C)")
    return formatted


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    try:
        if tests.__class__ is not list:
            raise ValueError(
                "Error: Tests input should be list of int")
        for i in tests:
            print(f"Testing temperature: {i}")
            try:
                if not i:
                    raise ValueError(
                        f"Error: '{i}' is not a valid number\n")
                formatted = check_temperature(i)
                print(
                    f"Temperature {formatted}°C is perfect for plants!\n")
            except ValueError as e:
                print(e, end="\n\n")
    except Exception as e:
        print(e)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(e)
