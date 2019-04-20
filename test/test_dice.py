"""
Title: test_dice
Author: Kevin Tracey McGee (DGNSREKT)
Date: 4/17/2019
Description: Tests the baseball_simulator dice function.
Url: https://github.com/nolapython/baseball
"""

from pathlib import Path
import sys
import random
import pytest

# Used to change to the correct directory to avoid import errors.
FILEPATH = Path(__file__).parent.parent
sys.path.insert(0, FILEPATH)

from baseball_simulator import dice  # pylint: disable=wrong-import-position


@pytest.fixture
def roll_dice_fixture():
    """
    Dice rolling fixture.
    Returns: 10 samples from the dice function appended to a list. -- [(int, int)]
    """
    random.seed(1)  # Used to make sure the results are deterministic.
    samples = []
    for _ in range(10):
        single_sample = dice()
        samples.append(single_sample)
    return samples


def test_dice_function_returns_list(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """Test the dice function returns a list."""
    samples = roll_dice_fixture
    for sample in samples:
        assert isinstance(sample, list)


def test_each_dice_returns_int(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """Test each dice sample is type int."""
    samples = roll_dice_fixture
    for sample in samples:
        assert isinstance(sample[0], int)
        assert isinstance(sample[1], int)


def test_each_dice_roll_greater_than_zero(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """Test each dice sample is greater than zero."""
    samples = roll_dice_fixture
    for sample in samples:
        _dice, _dice2 = sample
        assert _dice > 0
        assert _dice2 > 0


def test_each_dice_roll_less_than_or_equal_to_six(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """Test each dice roll is less than or equal to six."""
    samples = roll_dice_fixture
    for sample in samples:
        _dice, _dice2 = sample
        assert _dice <= 6
        assert _dice2 <= 6


def test_the_dice_is_sorted(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """Test dice output is sorted."""
    samples = roll_dice_fixture
    for sample in samples:
        _dice, _dice2 = sample
        assert _dice <= _dice2
