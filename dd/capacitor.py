from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex0.creature import Creature


def test_healing_factory() -> None:
    """Test healing Creature factory: describe, attack, heal."""
    factory = HealingCreatureFactory()
    print("Testing Creature with healing capability")

    for label, creature in [("base", factory.create_base()),
                             ("evolved", factory.create_evolved())]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform_factory() -> None:
    """Test transform Creature factory: describe, attack, transform, attack, revert."""
    factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")

    for label, creature in [("base", factory.create_base()),
                             ("evolved", factory.create_evolved())]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


if __name__ == "__main__":
    test_healing_factory()
    print()
    test_transform_factory()
