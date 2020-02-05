# -*- coding: utf-8 -*-

"""Contain game-prime logic."""

from random import randrange


DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no"')


def is_prime(num):
    """Primality Test for given number return boolean.

    Argument:
    num -- int number
    """
    if num <= 1:
        return False
    elif num >= 4:
        for divider in range(2, num):
            if num % divider == 0:
                return False
    return True


def logic():
    """Define logic for brain-prime game.

    return tuple of question, correct answer
    """
    question = randrange(100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, str(answer)
