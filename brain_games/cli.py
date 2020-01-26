# -*- coding: utf-8 -*-

"""functions for user interaction."""

import prompt


def ask(question, empty=True):
    """Ask question by prompt return answer.

    Keyword argument:
    empty -- permit empty answer
    """
    return prompt.string(question, empty=empty)


def say(phrase):
    """Print phrase to stdout"""
    print(phrase)


def welcome_user(game_description=None):
    """Greeting user, show game rules, ask user name return user name.

    Keyword argument:
    game_description -- show game description after greeting
    """
    say('Welcome to the Brain Games!')
    if game_description:
        say(game_description)
    name = ask('\nMay I have your name? ', False)
    say(f'Hello, {name}!\n')
    return name
