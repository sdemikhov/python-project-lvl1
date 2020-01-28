# -*- coding: utf-8 -*-

"""Contain game-progression logic."""

from random import randrange

from .game_base import game_base


game_progression_description = """
What number is missing in the progression?
"""


def arithmetic_progression(start, step, length, values_as_string=False):
    """Return arithmetic progression as list.

    Arguments:
    start -- first number in an arithmetic progression
    step -- common difference
    length -- number of terms in progression

    Keyword argument:
    values_as_string -- changes int to str in progression list
    """
    result = []
    num = start
    for _ in range(length):
        num += step
        result.append(num)
    if values_as_string:
        result = [str(i) for i in result]
    return result


def game_progression_logic():
    """Define logic for brain-progression game.

    return tuple of question, correct answer
    """
    prog_start = randrange(100)
    prog_step = randrange(1, 11)
    progression = arithmetic_progression(start=prog_start,
                                         step=prog_step,
                                         length=10,
                                         values_as_string=True)
    hide_num_idx = randrange(10)
    answer = progression.pop(hide_num_idx)
    progression.insert(hide_num_idx, '..')
    question = ' '.join(progression)
    return question, str(answer)


def game_progression():
    """Passes description and logic for brain-calc game to engine."""
    game_base(game_progression_description, game_progression_logic)
