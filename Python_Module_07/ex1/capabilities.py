from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0.factory import CreatureFactory


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class Sproutling(HealCapability, Creature):

    def __init__(self):
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(HealCapability, Creature):

    def __init__(self):
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCapability(ABC):

    def __init__(self):
        self.is_transforme = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(TransformCapability, Creature):

    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transforme:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def revert(self) -> str:
        self.is_transforme = False
        return f"{self.name} returns to normal."

    def transform(self) -> str:
        self.is_transforme = True
        return f"{self.name} shifts into a sharper form!"


class Morphagon(TransformCapability, Creature):

    def __init__(self):
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transforme:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def revert(self) -> str:
        self.is_transforme = False
        return f"{self.name} stabilizes its form."

    def transform(self) -> str:
        self.is_transforme = True
        return f"{self.name} morphs into a dragonic battle form!"


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
