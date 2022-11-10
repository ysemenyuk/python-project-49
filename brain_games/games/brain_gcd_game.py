import math
from brain_games.run_games import run_game
from brain_games.utils import getRandomInt

greeting = 'Find the greatest common divisor of given numbers.'


def get_data():
    num1 = getRandomInt()
    num2 = getRandomInt()
    question = f'{num1} {num2}'
    answer = str(math.gcd(num1, num2))
    return (question, answer)


def brain_gcd_game():
    run_game(greeting, get_data)
