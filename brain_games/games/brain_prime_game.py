# import math
from brain_games.run_games import run_game
from brain_games.utils import getRandomInt


greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def get_data():
    num = getRandomInt()
    question = f'{num}'
    answer = 'yes' if is_prime(num) else 'no'
    return (question, answer)


def brain_prime_game():
    run_game(greeting, get_data)
