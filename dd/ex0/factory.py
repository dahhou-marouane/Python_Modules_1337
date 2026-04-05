from abc import ABC, abstractmethod
from ex0.creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating Creature families."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base Creature of this family."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved Creature of this family."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for the Fire family: Flameling and Pyrodon."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for the Water family: Aquabub and Torragon."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
