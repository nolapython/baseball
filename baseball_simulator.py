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
