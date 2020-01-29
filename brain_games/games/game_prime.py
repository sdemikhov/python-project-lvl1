# -*- coding: utf-8 -*-

"""Contain game-prime logic."""

from random import randrange

from .game_base import game_base


GAME_PRIME_DESCRIPTION = """
Answer "yes" if given number is prime. Otherwise answer "no"
"""


def game_prime_logic():
    """Define logic for brain-prime game.

    return tuple of question, correct answer
    """
    question = randrange(100)
    answer = 'yes'
    if question <= 1:
        answer = 'no'
    elif question >= 4:
        for divider in range(2, question):
            if question % divider == 0:
                answer = 'no'
                break
    return question, str(answer)


def game_prime():
    """Passes description and logic for brain-prime game to engine."""
    game_base(GAME_PRIME_DESCRIPTION, game_prime_logic)
