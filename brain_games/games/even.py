# -*- coding: utf-8 -*-

"""Contain game-even logic."""

from random import randrange


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def logic():
    """Define logic for brain-even game, return question, answer"""
    num = randrange(100)
    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer
