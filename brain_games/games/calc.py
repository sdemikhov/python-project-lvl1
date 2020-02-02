# -*- coding: utf-8 -*-

"""Contain game-calc logic."""

from random import randrange, choice
from operator import add, mul, sub


DESCRIPTION = "What is the result of the expression?"


def logic():
    """Define logic for brain-calc game, return question, answer"""
    operators = {'+': add, '*': mul, '-': sub}
    num1, num2 = [randrange(100) for _ in range(2)]
    oper = choice([k for k in operators.keys()])
    question = f'{num1} {oper} {num2}'
    answer = operators[oper](num1, num2)
    return question, str(answer)
