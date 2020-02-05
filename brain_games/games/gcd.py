# -*- coding: utf-8 -*-

"""Contain game-gcd logic."""

from random import randrange


DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(num_left, num_right):
    """Return greatest common divisor of given numbers.

    Arguments:
    num_left -- int number
    num_right -- int number
    """
    b, a = sorted([num_left, num_right])
    i = 1
    while True:
        r = a - b * i
        if r == 0:
            return b
        elif r < b:
            i = 1
            a = b
            b = r
            continue
        i += 1


def logic():
    """Define logic for brain-gcd game, return question, answer"""
    num_left = randrange(100)
    num_right = randrange(100)
    question = f'{num_left} {num_right}'
    answer = gcd(num_left, num_right)
    return question, str(answer)
