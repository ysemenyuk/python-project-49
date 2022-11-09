import prompt
import random


def is_even(num):
    return num % 2 == 0


def even_game():
    name = prompt.string('May I have your name? ')
    print(f'Helloooooo, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        num = random.randint(1, 21)
        print(f'Question: {num}')
        user_answer = prompt.string('Your answer: ')
        answer = 'yes' if is_even(num) else 'no'
        if user_answer == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
