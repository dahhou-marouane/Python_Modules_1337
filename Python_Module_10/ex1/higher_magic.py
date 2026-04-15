from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


if __name__ == "__main__":
    target = "Dragon"
    power = 12

    print()

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    a, b = combined(target, power)
    print(f"Combined spell result: {a}, {b}")

    print()

    print("Testing power amplifier...")
    amplifier = power_amplifier(fireball, 3)
    print("Original:", fireball(target, power))
    print("Amplified:", amplifier(target, power))

    print()

    print("Testing conditional caster...")
    conditional = conditional_caster(lambda _, a: a >= 11, fireball)
    print("Power 10:", conditional(target, 10))
    print("Power 12:", conditional(target, 12))

    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for seq in sequence(target, power):
        print(seq)
