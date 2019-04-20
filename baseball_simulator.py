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

import plotly.offline as py
import plotly.figure_factory as ff


def dice():
    """
    Simulate rolling 2 standard 6 sided dice.
    Returns: [int, int] Returns the result of a dice roll
    """
    roll = (random.randint(1, 6), random.randint(1, 6))
    return sorted(roll)


class Runner:
    """
    Description: Simulates a runner moving through bases.
    """

    def __init__(self):
        self.base = 0

    def run_to_next_base(self):
        self.base += 1

    @property
    def has_scored(self):
        if self.base > 3:
            return True
        return False

    def __repr__(self):
        return f"< RUNNER > BASE:{self.base}"


class ActionMap:
    @classmethod
    def map_action_to_dice(cls, roll):
        map = {
            "11": cls.double,
            "12": cls.single,
            "13": cls.single,
            "14": cls.single,
            "15": cls.base_on_error,
            "16": cls.base_on_balls,
            "22": cls.strike,
            "23": cls.strike,
            "24": cls.strike,
            "25": cls.strike,
            "26": cls.foul_out,
            "33": cls.out_at_first,
            "34": cls.out_at_first,
            "35": cls.out_at_first,
            "36": cls.out_at_first,
            "44": cls.fly_out,
            "45": cls.fly_out,
            "46": cls.fly_out,
            "55": cls.double_play,
            "56": cls.triple,
            "66": cls.home_run,
        }
        return map[str(roll[0]) + str(roll[1])]

    @classmethod
    def single(cls, state):
        new_runner = Runner()
        state.add_runner_to_field(new_runner)
        for runner in state.field:
            runner.run_to_next_base()
        if runner.has_scored:
            state.remove_runner_from_field_after_scoring()
            state.score += 1

    @classmethod
    def double(cls, state):
        for _ in range(2):
            cls.single(state)

    @classmethod
    def base_on_error(cls, state):
        cls.single(state)

    @classmethod
    def base_on_balls(cls, state):
        cls.single(state)

    @classmethod
    def strike(cls, state):
        state.strikes += 1
        if state.strikes > 2:
            state.strikes = 0
            state.outs += 1

    @classmethod
    def foul_out(cls, state):
        state.outs += 1

    @classmethod
    def out_at_first(cls, state):
        state.outs += 1

    @classmethod
    def fly_out(cls, state):
        state.outs += 1

    @classmethod
    def double_play(cls, state):
        state.outs += 2
        state.remove_runner_from_field_after_out()

    @classmethod
    def triple(cls, state):
        for _ in range(3):
            cls.single(state)

    @classmethod
    def home_run(cls, state):
        for _ in range(4):
            cls.single(state)


class GameState:
    def __init__(self):
        self.field = deque()
        self.score = 0
        self.strikes = 0
        self.outs = 0
        self.plays = 0

    def add_runner_to_field(self, runner):
        self.field.appendleft(runner)

    def remove_runner_from_field_after_scoring(self):
        if len(self.field) > 0:
            self.field.pop()

    def remove_runner_from_field_after_out(self):
        if len(self.field) > 0:
            self.field.popleft()

    @property
    def is_done(self):
        """
        Description:
        Arguments:
            None
        Returns:
        """
        if self.outs >= 54:
            return True
        return False

    def __repr__(self):
        repr_str = "--GAME-STATE--\n"
        repr_str += f"RUNNERS: {list(self.field)}\n"
        repr_str += f"SCORE: {self.score}\n"
        repr_str += f"INNINGS: {self.innings}\n"
        repr_str += f"STRIKES: {self.strikes}\n"
        repr_str += f"OUTS: {self.outs}\n"
        repr_str += f"PLAYS: {self.plays}\n"
        return repr_str


class BaseballSimulator:
    """
    Description:
    Arguments:
        None
    Returns:
    """

    def __init__(self):
        self.state = GameState()

    def step(self, dice_roll, render=False):
        """
        Description:
        Arguments:
            None
        Returns:
        """
        executable_action = ActionMap.map_action_to_dice(dice_roll)
        executable_action(self.state)
        self.state.plays += 1
        if render:
            print(self.state)
        return self.state, self.state.is_done


def compute_average(list_of_scores):
    return sum(list_of_scores) / len(list_of_scores)


def render_plot(scores):
    hist_data = [scores]
    group_labels = ["RUNS per GAME"]

    fig = ff.create_distplot(hist_data, group_labels, show_rug=False)
    fig["layout"].update(title="Distribution of runs from nine inning games.")
    py.plot(fig, filename="chart.html")


def simulate_games(number_of_simulations):
    final_scores = []
    final_outs = []
    final_plays = []
    for _ in range(number_of_simulations):
        print(".", flush=True, end="")
        simulator = BaseballSimulator()
        while True:
            roll = dice()
            state, done = simulator.step(roll)
            if done:
                final_scores.append(state.score)
                final_outs.append(state.outs)
                final_plays.append(state.plays)
                break

    # average_scores = compute_average(final_scores)
    # average_outs = compute_average(final_outs)
    # average_plays = compute_average(final_plays)

    return final_scores, final_outs, final_plays


if __name__ == "__main__":
    n = 1000
    scores, outs, plays = simulate_games(n)
    render_plot(scores)
