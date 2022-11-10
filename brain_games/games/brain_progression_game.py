import math
from brain_games.run_games import run_game
from brain_games.utils import getRandomInt

greeting = 'What number is missing in the progression?'


def makeRandomProgression(length=7):
    start = getRandomInt()
    step = getRandomInt(2, 7)
    stop = start + length * step
    return list(range(start, stop, step))


def get_data():
    progression = makeRandomProgression()
    missing_num_index = getRandomInt(0, len(progression))

    missing_num = progression[missing_num_index]
    answer = str(missing_num)

    progression[missing_num_index] = '..'
    question = f'{" ".join([str(i) for i in progression])}'
    
    return (question, answer)


def brain_progression_game():
    run_game(greeting, get_data)
