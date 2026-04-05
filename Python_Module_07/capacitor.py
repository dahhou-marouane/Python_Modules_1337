from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex0.factory import CreatureFactory
from typing import cast
from ex1.capabilities import HealCapability
from ex0.creature import Creature
from ex1.capabilities import TransformCapability


def healing_test(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    base_heal: HealCapability = cast(HealCapability, base)
    print(base_heal.heal())
    print(" evolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    evolved_heal: HealCapability = cast(HealCapability, evolved)
    print(evolved_heal.heal())


def transform_test(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base: Creature = factory.create_base()
    base_tansform: TransformCapability = cast(TransformCapability, base)
    print(base.describe())
    print(base.attack())
    print(base_tansform.transform())
    print(base.attack())
    print(base_tansform.revert())
    print(" evolved:")
    evolved = factory.create_base()
    evolved_transform: TransformCapability = cast(TransformCapability, evolved)
    print(evolved.describe())
    print(evolved.attack())
    print(evolved_transform.transform())
    print(evolved.attack())
    print(evolved_transform.revert())


if __name__ == "__main__":
    factory1: CreatureFactory = HealingCreatureFactory()
    factory2: CreatureFactory = TransformCreatureFactory()
    healing_test(factory1)
    print()
    transform_test(factory2)
