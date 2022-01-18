from collections import Counter

import pytest

from src.simulator.base import Base
from src.simulator.dice import Dice, DiceValues



def test_dice_count():
    print("hellp")
    c = Counter({Dice(DiceValues.Monkey): 5, Dice(DiceValues.Diamond): 3})
    list_of_dice = list(c.elements())
    dice_map = Base.dice_count (list_of_dice)
    assert dice_map[DiceValues.Monkey] == 5
    assert dice_map[DiceValues.Diamond] == 3
    assert dice_map[DiceValues.Gold] == 0

