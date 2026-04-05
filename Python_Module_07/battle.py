from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    try:
        flame: CreatureFactory = FlameFactory()
        aqua: CreatureFactory = AquaFactory()
        test_factory(flame)
        print()
        test_factory(aqua)
        print()
        test_battle(flame, aqua)
    except Exception as e:
        print(e)
