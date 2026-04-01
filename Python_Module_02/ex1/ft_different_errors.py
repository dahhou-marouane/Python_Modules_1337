#!/usr/bin/env python3
def garden_operations() -> None:
    ages = {'Jim': 30, 'Pam': 28}
    file = 'missing.txt'
    print("Testing ValueError...")
    try:
        try:
            int("abc")
        except ValueError:
            raise ValueError('invalid literal for int()')
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught {type(e).__name__}: {e}\n")
    print("Testing FileNotFoundError...")
    try:
        try:
            x = open(file)
            if x:
                x.close()
            print(f"File {file} found")
        except FileNotFoundError:
            raise FileNotFoundError(f"No such file '{file}'")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("\nTesting KeyError...")
    try:
        print(ages['missing\\_plant'])
    except KeyError as e:
        print(f"Caught {type(e).__name__}: {e.args[0]}")
    print("\nTesting multiple errors together...")
    try:
        int("abc")
        10 / 0
        x = open(file)
        if x:
            x.close()
        print(ages['missing_plant'])
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        garden_operations()
    except Exception as e:
        print(f"Caught {type(e).__name__}: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(e)
