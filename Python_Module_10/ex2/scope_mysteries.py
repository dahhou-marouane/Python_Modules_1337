from collections.abc import Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def power_accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i}:", counter())
    counter = mage_counter()
    print("counter_b call 1:", counter())

    print()

    print("Testing spell accumulator...")
    spell = spell_accumulator(100)
    print("Base 100, add 20:", spell(20))
    print("Base 100, add 30:", spell(30))

    print()

    print("Testing enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    enchantment = enchantment_factory("Frozen")
    print(enchantment("Shield"))

    print()

    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault['recall']('secret'))
    print("Recall 'unknown':", vault["recall"]('unknown'))
