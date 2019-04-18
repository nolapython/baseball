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

# imported to changes to the correct directory for testing
FILEPATH = Path(__file__).parent.parent
sys.path.insert(0, FILEPATH)

from baseball_simulator import dice  # pylint: disable=wrong-import-position


@pytest.fixture
def roll_dice_fixture():
    """
    Description: Dice rolling fixture.
    Arguments:
        None
    Returns:
        10 samples from the dice function appended to a list. -- [(int, int)]
    """
    random.seed(1)  # Used to make sure the resutls are deterministic.
    samples = []
    for _ in range(10):
        single_sample = dice()
        samples.append(single_sample)
    return samples


def test_dice_function_returns_list(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """
    Description: Test the dice function returns a list.
    Arguments:
        None
    Returns:
        None
    """
    samples = roll_dice_fixture
    for sample in samples:
        assert isinstance(sample, list)


def test_each_dice_returns_int(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """
    Description: Test each dice sample is of type int.
    Arguments:
        None
    Returns:
        None
    """
    samples = roll_dice_fixture
    for sample in samples:
        assert isinstance(sample[0], int)
        assert isinstance(sample[1], int)


def test_each_dice_roll_greater_than_zero(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """
    Description: Test each dice sample is greater than zero.
    Arguments:
        None
    Returns:
        None
    """
    samples = roll_dice_fixture
    for sample in samples:
        _dice, _dice2 = sample
        assert _dice > 0
        assert _dice2 > 0


def test_each_dice_roll_less_than_or_equal_to_six(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """
    Description: Test each dice roll is less than or equal to six.
    Arguments:
        None
    Returns:
        None
    """
    samples = roll_dice_fixture
    for sample in samples:
        _dice, _dice2 = sample
        assert _dice <= 6
        assert _dice2 <= 6


def test_the_dice_is_sorted(roll_dice_fixture):
    # pylint: disable=redefined-outer-name
    """
    Description: Test dice output is sorted.
    Arguments:
        None
    Returns:
        None
    """
    samples = roll_dice_fixture
    for sample in samples:
        _dice, _dice2 = sample
        assert _dice <= _dice2
