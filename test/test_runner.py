"""
Title: test_dice
Author: Kevin Tracey McGee (DGNSREKT)
Date: 4/18/2019
Description: Tests the baseball_simulator runner class.
Url: https://github.com/nolapython/baseball
"""

from pathlib import Path
import sys
import random
import pytest

# Used to change to the correct directory to avoid import errors.
FILEPATH = Path(__file__).parent.parent
sys.path.insert(0, FILEPATH)

from baseball_simulator import Runner  # pylint: disable=wrong-import-position


@pytest.fixture
def runner_fixture():
    """
    Runner fixture.
    Returns: Runner Object
    """
    return Runner()


def test_run_to_next_base(runner_fixture):
    """Test the runner moves to the next base."""
    runner = runner_fixture
    assert runner.base == 0
    runner.run_to_next_base()
    assert runner.base == 1


def test_has_scored(runner_fixture):
    """Test after running to the next base 4 times The runner has scored."""
    runner = runner_fixture
    assert runner.has_scored == False
    runner.run_to_next_base()
    runner.run_to_next_base()
    runner.run_to_next_base()
    runner.run_to_next_base()
    assert runner.has_scored == True
