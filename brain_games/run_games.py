import prompt


def run_game(greeting, get_round_data):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(greeting)

    max_runds = 3
    correct_answers = 0

    while correct_answers < max_runds:
        question, answer = get_round_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
