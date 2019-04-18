"""
Title: baseball_simulator
Author: Kevin Tracey McGee (DGNSREKT)
Date: 4/17/2019
Description: Baseball + Yahtzee: A baseball simulator which uses
two standard dice to simulate the outcomes of a baseball game.
Url: https://github.com/nolapython/baseball

Goals:
1. Find the average number of runs that would be scored in 9 innings.
2. Find the distribution of the number of runs scored across multiple
simulated games.
"""
import random
from collections import deque


def dice():
    """
    Description: Simulate rolling 2 standard 6 sided dice.
    Arguments:
        None
    Returns:
        Result of the dice roll. -- [int, int]
    """
    roll = (random.randint(1, 6), random.randint(1, 6))
    return sorted(roll)


class Runner:
    """
    Description:
    Arguments:
        None
    Returns:
    """

    def __init__(self):
        self.current_base = 0

    def run(self):
        pass

    def has_scored(self):
        pass


class BaseballSimulator:
    """
    Description:
    Arguments:
        None
    Returns:
    """

    def __init__(self):
        self.field = deque()
        self.innings = 0
        self.strikes = 0
        self.outs = 0
        self.plays = 0

    def map_dice_action(self, dice):
        """
        Description:
        Arguments:
            None
        Returns:
        """
        pass

    def step(self, action):
        """
        Description:
        Arguments:
            None
        Returns:
        """
        pass

    def done(self):
        """
        Description:
        Arguments:
            None
        Returns:
        """
        pass
