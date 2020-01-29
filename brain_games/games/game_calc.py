# -*- coding: utf-8 -*-

"""Contain game-calc logic."""

from random import randrange, choice
from operator import add, mul, sub

from .game_base import game_base


GAME_CALC_DESCRIPTION = "What is the result of the expression?"


def game_calc_logic():
    """Define logic for brain-calc game, return question, answer"""
    operators = {'+': add, '*': mul, '-': sub}
    num1, num2 = [randrange(100) for _ in range(2)]
    oper = choice([k for k in operators.keys()])
    question = f'{num1} {oper} {num2}'
    answer = operators[oper](num1, num2)
    return question, str(answer)


def game_calc():
    """Passes description and logic for brain-calc game to engine."""
    game_base(GAME_CALC_DESCRIPTION, game_calc_logic)
