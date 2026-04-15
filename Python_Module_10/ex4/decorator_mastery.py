import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"Spell completed in {end:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if not kwargs.get('power'):
                power = args[-1]
            else:
                power = kwargs['power']
            if not isinstance(power, int):
                return "No power found"
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@retry_spell(3)
def tester() -> None:
    raise ValueError


if __name__ == "__main__":
    print("Testing spell timer...")
    print("Result:", fireball())

    print()

    print("Testing retrying spell...")
    print(tester())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(MageGuild.validate_mage_name("marouane"))
    print(MageGuild.validate_mage_name("marouane1"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 9))
