# -*- coding: utf-8 -*-

"""Contain games logic"""

from random import randrange

from .cli import welcome_user, ask, say


def game_even(wins_max=3, num_min=0, num_max=99):
    game_description = """
    Answer "yes" if number even otherwise answer "no".
    """
    username = welcome_user(game_description.strip())
    wins = 0
    while (wins < wins_max):
        num = randrange(num_min, num_max)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        say(f'Question: {num}')
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
