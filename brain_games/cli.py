# -*- coding: utf-8 -*-

"""functions for user interaction."""

import prompt


def welcome_user():
    """Ask user's name.return welcome string."""
    name = prompt.string('May I have your name? ')
    return 'Hello, {name}!'.format(name=name)
