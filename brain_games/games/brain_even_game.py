from brain_games.run_games import run_game
from brain_games.utils import getRandomInt

greeting = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_data():
    random_num = getRandomInt()
    question = str(random_num)
    answer = 'yes' if is_even(random_num) else 'no'
    return (question, answer)


def brain_even_game():
    run_game(greeting, get_data)
