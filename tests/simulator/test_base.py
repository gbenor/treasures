from collections import Counter

import pytest

from src.simulator.base import Base
from src.simulator.dice import Dice, DiceValues


def test_dice_count():
    c = Counter({Dice(DiceValues.Monkey): 5, Dice(DiceValues.Diamond): 3})
    list_of_dice = list(c.elements())
    dice_map = Base.dice_count(list_of_dice)
    assert dice_map[DiceValues.Monkey] == 5
    assert dice_map[DiceValues.Diamond] == 3
    assert dice_map[DiceValues.Gold] == 0


def test_false_is_full_box():
    for c in [Counter({Dice(DiceValues.Monkey): 7,
                       Dice(DiceValues.Diamond): 0,
                       Dice(DiceValues.Gold): 0,
                       Dice(DiceValues.Sword): 0,
                       Dice(DiceValues.Skull): 1,
                       Dice(DiceValues.Banana): 0}),
              Counter({Dice(DiceValues.Monkey): 6,
                       Dice(DiceValues.Diamond): 0,
                       Dice(DiceValues.Gold): 1,
                       Dice(DiceValues.Sword): 1,
                       Dice(DiceValues.Skull): 0,
                       Dice(DiceValues.Banana): 0}),
              Counter({Dice(DiceValues.Monkey): 0,
                       Dice(DiceValues.Diamond): 4,
                       Dice(DiceValues.Gold): 2,
                       Dice(DiceValues.Sword): 2,
                       Dice(DiceValues.Skull): 0,
                       Dice(DiceValues.Banana): 0})
              ]:
        list_of_dice = list(c.elements())
        dice_map = Base.dice_count(list_of_dice)
        assert not Base.is_full_box(dice_map)


def test_true_is_full_box():
    for c in [Counter({Dice(DiceValues.Monkey): 4,
                       Dice(DiceValues.Diamond): 0,
                       Dice(DiceValues.Gold): 0,
                       Dice(DiceValues.Sword): 4,
                       Dice(DiceValues.Skull): 0,
                       Dice(DiceValues.Banana): 0}),
              Counter({Dice(DiceValues.Monkey): 3,
                       Dice(DiceValues.Diamond): 2,
                       Dice(DiceValues.Gold): 3,
                       Dice(DiceValues.Sword): 0,
                       Dice(DiceValues.Skull): 0,
                       Dice(DiceValues.Banana): 0}),
              Counter({Dice(DiceValues.Monkey): 0,
                       Dice(DiceValues.Diamond): 4,
                       Dice(DiceValues.Gold): 4,
                       Dice(DiceValues.Sword): 0,
                       Dice(DiceValues.Skull): 0,
                       Dice(DiceValues.Banana): 0})
              ]:
        list_of_dice = list(c.elements())
        dice_map = Base.dice_count(list_of_dice)
        assert Base.is_full_box(dice_map)


def test_score():
    turn = Base()
    for (c, s) in [(Counter({Dice(DiceValues.Monkey): 4,
                             Dice(DiceValues.Diamond): 0,
                             Dice(DiceValues.Gold): 0,
                             Dice(DiceValues.Sword): 4,
                             Dice(DiceValues.Skull): 0,
                             Dice(DiceValues.Banana): 0}), 500 + 200 + 200),
                   (Counter({Dice(DiceValues.Monkey): 3,
                             Dice(DiceValues.Diamond): 2,
                             Dice(DiceValues.Gold): 3,
                             Dice(DiceValues.Sword): 0,
                             Dice(DiceValues.Skull): 0,
                             Dice(DiceValues.Banana): 0}), 500 + 100 + 200 + 400),
                   (Counter({Dice(DiceValues.Monkey): 0,
                             Dice(DiceValues.Diamond): 4,
                             Dice(DiceValues.Gold): 4,
                             Dice(DiceValues.Sword): 0,
                             Dice(DiceValues.Skull): 0,
                             Dice(DiceValues.Banana): 0}), 500 + 600 + 600),
                   (Counter({Dice(DiceValues.Monkey): 0,
                             Dice(DiceValues.Diamond): 4,
                             Dice(DiceValues.Gold): 1,
                             Dice(DiceValues.Sword): 0,
                             Dice(DiceValues.Skull): 3,
                             Dice(DiceValues.Banana): 0}), 0),

                   ]:
        list_of_dice = list(c.elements())
        assert turn.score(list_of_dice) == s
