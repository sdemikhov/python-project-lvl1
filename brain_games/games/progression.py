# -*- coding: utf-8 -*-

"""Contain game-progression logic."""

from random import randrange


DESCRIPTION = "What number is missing in the progression?"


def arithmetic_progression(start, step, length):
    """Return arithmetic progression as list of str.

    Arguments:
    start -- first number in an arithmetic progression
    step -- common difference
    length -- number of terms in progression
    """
    num_last = start + (length - 1) * step
    return [str(num) for num in range(start, num_last+1, step)]


PROG_LENGTH = 10


def logic():
    """Define logic for brain-progression game.

    return tuple of question, correct answer
    """
    prog_start = randrange(100)
    prog_step = randrange(1, 11)
    progression = arithmetic_progression(start=prog_start,
                                         step=prog_step,
                                         length=PROG_LENGTH)
    hide_num_idx = randrange(10)
    answer = progression.pop(hide_num_idx)
    progression.insert(hide_num_idx, '..')
    question = ' '.join(progression)
    return question, str(answer)
