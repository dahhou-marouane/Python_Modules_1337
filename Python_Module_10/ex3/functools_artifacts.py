from functools import reduce, partial, lru_cache, singledispatch
from operator import mul, add
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable] = {
        "add": add,
        "max": max,
        "min": min,
        "multiply": mul
    }
    if operation not in operations:
        raise ValueError(f"Error: Unknown operation '{operation}'")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "sword": partial(base_enchantment, 50, "Sword"),
        "arrow": partial(base_enchantment, 50, "Arrow")
    }


def base_enchant(power: int, element: str, target: str) -> str:
    return f"{element} hits {target} (power={power})"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell_data: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell_data: int) -> str:
        return f"Damage spell: {spell_data} damage"

    @dispatch.register
    def _(spell_data: str) -> str:
        return f"Enchantment: {spell_data}"

    @dispatch.register
    def _(spell_data: list) -> str:
        return f"Multi-cast: {len(spell_data)} spells"
    return dispatch


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    values = [10, 20, 30, 40]
    try:
        print("Sum:", spell_reducer(values, "add"))
        print("Product:", spell_reducer(values, "multiply"))
        print("Max:", spell_reducer(values, "max"))
    except ValueError as e:
        print(e)

    print("\nTesting memoized fibonacci...")
    try:
        print("Fib(0):", memoized_fibonacci(0))
        print("Fib(1):", memoized_fibonacci(1))
        print("Fib(10):", memoized_fibonacci(10))
        print("Fib(15):", memoized_fibonacci(15))
    except RecursionError as e:
        print("Recursion limit hit:", e)

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["a", "b", "c"]))
    print(dispatcher(None))
