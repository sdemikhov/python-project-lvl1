# -*- coding: utf-8 -*-

"""Contain game engine."""

from brain_games.cli import welcome_user, ask, say


def run(game):
    """Define game engine.

    Argument:
    game -- module than contains description and game logic
    """
    username = welcome_user(game.DESCRIPTION.strip())
    wins = 0
    while (wins < 3):
        question, correct_answer = game.logic()
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
