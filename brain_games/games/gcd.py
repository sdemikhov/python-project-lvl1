# -*- coding: utf-8 -*-

"""Contain game-gcd logic."""

from random import randrange
from math import gcd


DESCRIPTION = """
Find the greatest common divisor of given numbers.
"""


def logic():
    """Define logic for brain-gcd game, return question, answer"""
    num1, num2 = [randrange(100) for _ in range(2)]
    question = f'{num1} {num2}'
    answer = gcd(num1, num2)
    return question, str(answer)
