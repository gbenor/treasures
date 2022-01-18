from collections import Counter
from typing import List

import typing

from src.simulator.consts import GOLD_SCORE, NUM_OF_DICE, SCORE_DICT
from src.simulator.dice import Dice, DiceValues


class Base:
    """This class implements the logic of a regular turn. Special cases such as captain, angel, skull and etc should
    inherit from this class and update its functions. """
    @staticmethod
    def dice_count(dice_list: List[Dice]) -> typing.Counter[Dice]:
        assert len(dice_list) == NUM_OF_DICE, f"wrong number of dices: {len(dice_list)} != {NUM_OF_DICE}"
        return Counter(map(lambda c: c.value, dice_list))

    @staticmethod
    def is_full_box(dice_map: typing.Counter[Dice]) -> bool:
        """Check that each of the dices gives score"""
        if dice_map[DiceValues.Skull] > 0:
            return False
        for dice_value in [DiceValues.Banana, DiceValues.Monkey, DiceValues.Sword]:
            if 1 <= dice_map[dice_value] <= 2:
                return False
        return True

    def score(self, dice_list: List[Dice]) -> int:
        dice_map = self.dice_count(dice_list)
        if dice_map[DiceValues.Skull] >= 3:
            return 0
        score: int = 0
        for val, count in dice_map.items():
            if val != DiceValues.Skull:
                score += SCORE_DICT[count]
        score += GOLD_SCORE * (dice_map[DiceValues.Gold] + dice_map[DiceValues.Diamond])
        if self.is_full_box(dice_map):
            score += 500
        return score
