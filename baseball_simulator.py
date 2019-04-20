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
    Simulates rolling 2 standard 6 sided dice.
    Returns: [int, int] Returns the result of a dice roll
    """
    roll = (random.randint(1, 6), random.randint(1, 6))
    return sorted(roll)


class Runner:
    """Simulates a player hitting the ball and advancing through the bases."""

    def __init__(self):
        self.base = 0

    def run_to_next_base(self):
        """Advances the player to the next base."""
        self.base += 1

    @property
    def has_scored(self):
        """
        Checks if the runner has scored.
        Returns: True if player has scored.
        """
        if self.base > 3:
            return True
        return False

    def __repr__(self):
        return f"< RUNNER > BASE:{self.base}"


class ActionMap:
    """Provides a map of all the functions needed to simulate a game of baseball."""

    @classmethod
    def map_dice_roll_to_action(cls, roll):
        """
        Converts the roll to a string then matches the roll with the proper method.
        Args: roll [int, int] - A dice roll.
        Returns: function which simulates an action in a baseball game.
        """
        roll_to_str = str(roll[0]) + str(roll[1])  # converts [1, 1] to "11"

        action_map = {
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
        return action_map[roll_to_str]

    @classmethod
    def single(cls, state):
        """
        Simulates the player hitting the ball and advancing one base.
        Sets the strikes to 0.
        Creates a new Runner Object.
        Appends the new Runner to the GameState.field.
        Iterates through each Runner and updates the base position.
        Checks if the Runner has reached the home plate.
        If the Runner has scored the Runner is removed from the field and the scores is increased.
        Args: GameState Object.
        """
        scored = False
        state.strikes = 0
        new_runner = Runner()
        state.add_runner_to_field(new_runner)

        for runner in state.field:
            runner.run_to_next_base()
            if runner.has_scored:
                scored = True
        if scored:
            state.remove_runner_from_field_after_scoring()
            state.score += 1

    @classmethod
    def double(cls, state):
        """
        Runs the single function twice simulating a double.
        Args: GameState Object.
        """
        for _ in range(2):
            cls.single(state)

    @classmethod
    def base_on_error(cls, state):
        """
        Runs the single function simulating a base on error.
        Args: GameState Object.
        """
        cls.single(state)

    @classmethod
    def base_on_balls(cls, state):
        """
        Runs the single function simulating a base on balls.
        Args: GameState Object.
        """
        cls.single(state)

    @classmethod
    def strike(cls, state):
        """
        Simulates the player at bat missing the ball.
        GameStates.strikes is increased by 1.
        If the player has 3 strikes. GameState.outs is increased by 1.
        Args: GameState Object.
        """
        state.strikes += 1
        if state.strikes > 2:
            state.strikes = 0
            state.outs += 1

    @classmethod
    def foul_out(cls, state):
        """
        Simulates the player at bat fouling out.
        GameState.outs is increased by 1.
        Args: GameState Object
        """

        state.outs += 1

    @classmethod
    def out_at_first(cls, state):
        """
        Simulates the player getting taken out at first.
        GameState.outs is increased by 1.
        Args: GameState Object
        """
        state.outs += 1

    @classmethod
    def fly_out(cls, state):
        """
        Simulates a flyout.
        GameState.outs is increased by 1.
        Args: GameState Object
        """
        state.outs += 1

    @classmethod
    def double_play(cls, state):
        """
        Simulates the defense catching the ball and throwing it too first.
        GameState.outs is increased by 2.
        The last runner is removed from the field.
        Args: GameState Object
        """
        state.outs += 2
        state.remove_runner_from_field_after_out()

    @classmethod
    def triple(cls, state):
        """
        Runs the single function three times simulating a triple.
        Args: GameState Object.
        """
        for _ in range(3):
            cls.single(state)

    @classmethod
    def home_run(cls, state):
        """
        Runs the single function four times simulating a home run.
        Args: GameState Object.
        """
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

    def clear_the_field(self):
        self.field = deque()

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

    @property
    def half_inning_over(self):
        if self.outs % 3 == 0:
            return True
        return False

    def __repr__(self):
        repr_str = "--GAME-STATE--\n"
        repr_str += f"RUNNERS: {list(self.field)}\n"
        repr_str += f"SCORE: {self.score}\n"
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

    def step(self, dice_roll):
        """
        Description:
        Arguments:
            None
        Returns:
        """
        executable_action = ActionMap.map_dice_roll_to_action(dice_roll)
        executable_action(self.state)
        self.state.plays += 1
        return self.state, self.state.is_done


def compute_average(list_of_scores):
    return sum(list_of_scores) / len(list_of_scores)


def render_plot(scores):
    hist_data = [scores]
    group_labels = ["RUNS per GAME"]

    fig = ff.create_distplot(hist_data, group_labels, show_rug=False)
    fig["layout"].update(title="Distribution of runs from nine inning games.")
    py.plot(fig, filename="chart.html")


def simulate_games(number_of_simulations, render=False):
    final_scores = []
    final_outs = []
    final_plays = []
    for _ in range(number_of_simulations):
        if not render:
            print(".", flush=True, end="")
        simulator = BaseballSimulator()
        while True:
            roll = dice()
            state, done = simulator.step(roll)
            if render:
                print(state)

            if state.half_inning_over:
                state.clear_the_field()

            if done:
                final_scores.append(state.score)
                final_outs.append(state.outs)
                final_plays.append(state.plays)
                break

    return final_scores, final_outs, final_plays


if __name__ == "__main__":
    n = 1000
    scores, outs, plays = simulate_games(n, render=True)
    average_scores = compute_average(scores)
    average_outs = compute_average(outs)
    average_plays = compute_average(plays)
    print()
    print("AVERAGE SCORE:", average_scores)
    print("AVERAGE OUTS:", average_outs)
    print("AVERAGE PLAYS:", average_plays)
    render_plot(scores)
