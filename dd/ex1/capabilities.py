from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0.factory import CreatureFactory


class HealCapability(ABC):
    """Abstract capability for healing."""

    @abstractmethod
    def heal(self) -> str:
        """Perform a heal action and return a description."""
        pass


class TransformCapability(ABC):
    """Abstract capability for transforming."""

    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Transform and return a description."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Revert transformation and return a description."""
        pass


class Sproutling(Creature, HealCapability):
    """Base Grass-type Creature with healing capability."""

    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Evolved Grass/Fairy-type Creature with healing capability."""

    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Base Normal-type Creature with transform capability."""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved Normal/Dragon-type Creature with transform capability."""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    """Factory for the Healing family: Sproutling and Bloomelle."""

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory for the Transform family: Shiftling and Morphagon."""

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
