# -*- coding: utf-8 -*-

"""Contain game-even logic."""

from random import randrange

from .game_base import game_base


GAME_EVEN_DESCRIPTION = """
Answer "yes" if number even otherwise answer "no".
"""


def game_even_logic():
    """Define logic for brain-even game, return question, answer"""
    num = randrange(100)
    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer


def game_even():
    """Passes description and logic for brain-even game to engine."""
    game_base(GAME_EVEN_DESCRIPTION, game_even_logic)
