# -*- coding: utf-8 -*-

"""Contain game-calc logic."""

from random import randrange, choice
from operator import add, mul, sub


DESCRIPTION = "What is the result of the expression?"


OPERATORS = [('+', add),
             ('-', sub),
             ('*', mul)]


def logic():
    """Define logic for brain-calc game, return question, answer"""
    _operator, function = choice(OPERATORS)
    number_left = randrange(100)
    number_right = randrange(100)
    question = f'{number_left} {_operator} {number_right}'
    answer = function(number_left, number_right)
    return question, str(answer)
