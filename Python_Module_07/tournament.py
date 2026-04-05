from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1.capabilities import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print()
            print("* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except ValueError as e:
                print("Battle error, aborting tournament:", e)
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    Aggressive = AggressiveStrategy()
    Defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), Defensive)
        ])

    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), Aggressive),
        (HealingCreatureFactory(), Defensive)
        ])

    print()
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), Defensive),
        (TransformCreatureFactory(), Aggressive)
        ])
