from dataclasses import dataclass
from enum import Enum, auto


class DiceValues(Enum):
    Monkey = auto()
    Gold = auto()
    Diamond = auto()
    Banana = auto()
    Skull = auto()
    Sword = auto()


@dataclass(unsafe_hash=True)
class Dice:
    value: DiceValues
