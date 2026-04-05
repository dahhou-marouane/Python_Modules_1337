from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    """Abstract strategy for how a Creature acts in battle."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if this strategy is suitable for the given Creature."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Execute the strategy for the given Creature."""
        pass


class NormalStrategy(BattleStrategy):
    """Strategy: simply attack. Valid for any Creature."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy: transform, attack, revert. Valid for TransformCapability Creatures."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        tc = creature  # type: ignore[assignment]
        print(tc.transform())  # type: ignore[union-attr]
        print(creature.attack())
        print(tc.revert())  # type: ignore[union-attr]


class DefensiveStrategy(BattleStrategy):
    """Strategy: attack then heal. Valid for HealCapability Creatures."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())  # type: ignore[union-attr]
