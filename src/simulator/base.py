from collections import Counter
from typing import List

import typing

from src.simulator.consts import NUM_OF_DICE
from src.simulator.dice import Dice


class Base:
    @staticmethod
    def dice_count(dice_list: List[Dice]) -> typing.Counter[Dice]:
        assert len(dice_list) == NUM_OF_DICE, f"missing dices: {len(dice_list)} != {NUM_OF_DICE}"
        return Counter(map(lambda c:c.value, dice_list))

