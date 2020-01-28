# -*- coding: utf-8 -*-

"""functions for user interaction."""

import prompt


def ask(question, empty=True):
    """Ask question by prompt return answer.

    Argument:
    question -- string contain question

    Keyword argument:
    empty -- permit empty user input
    """
    answer = prompt.string(question, empty=empty)
    if answer is None:
        answer = ''
    return answer


def say(phrase):
    """Print phrase to stdout."""
    print(phrase)


def welcome_user(description=None):
    """Greeting user, show game rules, ask user name return user name.

    Keyword argument:
    description -- string contain game description
    """
    say('Welcome to the Brain Games!')
    if description:
        say(description)
    name = ask('\nMay I have your name? ', False)
    say(f'Hello, {name}!\n')
    return name
