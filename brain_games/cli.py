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


def welcome_user(description=None):
    """Greeting user, show game rules, ask user name return user name.

    Keyword argument:
    description -- string contain game description
    """
    print('Welcome to the Brain Games!')
    if description:
        print(description)
    name = ask('\nMay I have your name? ', False)
    print(f'Hello, {name}!\n')
    return name
