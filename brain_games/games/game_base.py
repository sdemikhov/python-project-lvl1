# -*- coding: utf-8 -*-

"""Contain base game logic."""

from ..cli import welcome_user, ask, say


def game_base(description, game_logic, wins_max=3):
    """Define game engine.

    Arguments:
    description -- string contain game description
    game_logic -- function than return question and correct answer

    Keyword argument:
    wins_max -- int rounds the user must win in a row
    """
    username = welcome_user(description.strip())
    wins = 0
    while (wins < wins_max):
        question, correct_answer = game_logic()
        say(f'Question: {question}')
        user_answer = ask(f'Your answer: ')
        if user_answer == correct_answer:
            say('Correct!')
            wins += 1
        else:
            say(f"'{user_answer}' is wrong answer ;(. Correct answer"
                f" was '{correct_answer}'. "
                f"Let's try again, {username}!")
            wins = 0
    say(f"Congratulations, {username}!")

