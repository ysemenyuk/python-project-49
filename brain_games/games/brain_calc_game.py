import random
from brain_games.run_games import run_game


greeting = 'What is the result of the expression?'
operators = ['+', '-', '*']


def calculate(num1, num2, operand):
    if operand == '+':
        return str(num1 + num2)
    elif operand == '-':
        return str(num1 - num2)
    elif operand == '*':
        return str(num1 * num2)


def get_data():
    operator = random.choice(operators)
    num1 = random.randint(1, 21)
    num2 = random.randint(1, 21)
    question = f'{num1} {operator} {num2}'
    answer = calculate(num1, num2, operator)
    return (question, answer)


def brain_calc_game():
    run_game(greeting, get_data)
