"""
Module 1: A module that rolls two dice, and is an effective random number generator.
Note that this is not something that will return some number between 2 and 12;
it will return two individual numbers between 1 and 6 that will be combined as a set.
As Ed pointed out earlier, it doesn't seem to matter the order the dice show up in,
i.e. 1, 2 gives you the same outcome as 2, 1.
"""

from pathlib import Path
import pytest
import sys

# imported to changes to the correct directory
FILEPATH = Path(__file__).parent.parent
sys.path.insert(0, FILEPATH)

from baseball import dice
import random


@pytest.fixture
def roll_dice_fixture():
    # Takes 10 samples from the dice function.
    random.seed(1)
    samples = []
    for _ in range(10):
        single_sample = dice()
        samples.append(single_sample)
    return samples


def test_dice_function_returns_tuple(roll_dice_fixture):
    samples = roll_dice_fixture
    for sample in samples:
        assert isinstance(sample, tuple)


def test_each_dice_returns_int(roll_dice_fixture):
    samples = roll_dice_fixture
    for sample in samples:
        assert isinstance(sample[0], int)
        assert isinstance(sample[1], int)


def test_each_dice_roll_greater_than_zero(roll_dice_fixture):
    samples = roll_dice_fixture
    for sample in samples:
        dice, dice2 = sample
        assert dice > 0
        assert dice2 > 0


def test_each_dice_roll_less_than_or_equal_to_six(roll_dice_fixture):
    samples = roll_dice_fixture
    for sample in samples:
        dice, dice2 = sample
        assert dice <= 6
        assert dice2 <= 6
