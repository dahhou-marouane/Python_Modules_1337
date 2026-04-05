from abc import ABC, abstractmethod

class BattleStrategy(ABC):

    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self) -> None:
        pass

    def is_valid(self) -> bool:
        pass



class AggressiveStrategy(BattleStrategy):

    def act(self) -> None:
        pass

    def is_valid(self) -> bool:
        pass


class DefensiveStrategy(BattleStrategy):

    def act(self) -> None:
        pass

    def is_valid(self) -> bool:
        pass

