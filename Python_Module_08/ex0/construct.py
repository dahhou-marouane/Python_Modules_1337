import sys
import site
import os


def out_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def in_venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print("Current Python:", sys.executable)
    print("Virtual Environment:",
          os.environ['VIRTUAL_ENV_PROMPT'].strip(" ()"))
    print("Environment Path:", sys.prefix)
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting\nthe global system.")
    print()
    print("Package installation path:")
    print(site.getsitepackages()[0])


if __name__ == "__main__":
    if sys.base_prefix != sys.prefix:
        in_venv()
    else:
        out_venv()
