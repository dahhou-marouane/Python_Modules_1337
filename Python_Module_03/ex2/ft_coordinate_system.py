import sys
import math


def math_sqrt(position: tuple[int, int, int]) -> float:
    default_coordinate: tuple[int, int, int] = (0, 0, 0)
    x1, y1, z1 = position
    x2, y2, z2 = default_coordinate
    return float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def ft_coordinate_system() -> None:
    default_tup: tuple[int, int, int] = (10, 20, 5)
    default_coordinate: tuple[int, int, int] = (0, 0, 0)
    print("=== Game Coordinate System ===\n")
    argc = len(sys.argv)
    if argc == 1:
        print(f"Position created: {default_tup}")
        x1, y1, z1 = default_tup
        print(
            f"Distance between {default_coordinate} and {default_tup}: "
            f"{math_sqrt(default_tup):.2f}")
    else:
        pos: tuple[int, int, int]
        args: list[str] = []
        for i in sys.argv[1:]:
            args += (i.split(","))
        if len(args) == 3:
            try:
                x1, y1, z1 = args
                x1 = int(x1)
                y1 = int(y1)
                z1 = int(z1)
                pos = x1, y1, z1
                print(f"Parsing coordinates: \"{x1},{y1},{z1}\"")
                print(f"Parsed position: {pos}")
            except ValueError as e:
                print(f"Parsing invalid coordinates: \"{x1},{y1},{z1}\"")
                print("Error parsing coordinates:", *e.args)
                print(
                    f"Error details - Type: {e.__class__.__name__}, "
                    f"Args: {e.args}")
                return
            print(f"Distance between {default_coordinate} and {pos}: "
                  f"{math_sqrt(pos):.1f}")
            print("\nUnpacking demonstration:")
            print(f"Player at x={x1}, y={y1}, z={z1}")
            print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")
        elif len(args) < 3 or len(args) > 3:
            print(
                "Error: args should be 3;\nUsage example: python3.10 "
                "ft_coordinate_system.py '\"3,4,0\" or 3 4 0'")


if __name__ == "__main__":
    ft_coordinate_system()
