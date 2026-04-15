from abc import ABC, abstractmethod
from ex1.capabilities import TransformCapability, HealCapability
from ex0.creature import Creature
from typing import cast


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' for this normal strategy")
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy")
        creature_trans: TransformCapability
        creature_trans = cast(TransformCapability, creature)
        print(creature_trans.transform())
        print(creature.attack())
        print(creature_trans.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy")
        print(creature.attack())
        creature_heal: HealCapability = cast(HealCapability, creature)
        print(creature_heal.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
