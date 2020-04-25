# -*- coding: utf-8 -*-

"""Contain game engine."""

from brain_games.cli import welcome_user, ask


MAX_WINS = 3


def run(game):
    """Define game engine.

    Argument:
    game -- module than contains description and game logic
    """
    username = welcome_user(game.DESCRIPTION)
    wins = 0
    while wins < MAX_WINS:
        question, correct_answer = game.logic()
        print(f'Question: {question}')
        user_answer = ask(f'Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer"
                f" was '{correct_answer}'. "
                f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
