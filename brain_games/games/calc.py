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
    oper, function = choice(OPERATORS)
    num_left = randrange(100)
    num_right = randrange(100)
    question = f'{num_left} {oper} {num_right}'
    answer = function(num_left, num_right)
    return question, str(answer)
