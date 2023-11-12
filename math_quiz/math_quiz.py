import random


def get_random_integer_between(min, max):
    """ 
    random integer generator
    use this to get a random integer between the given range

    :param min: lower limit of the range
    :param max: higher limit of the range
    :returns: a random integer between the higher and lower limit
    """
    return random.randint(min, max)


def get_random_operator():
    """ 
    random operator generator
    use this to get a random operator
    :returns: the random operator as a char; '+', '-' or '*'
    """
    return random.choice(['+', '-', '*'])


def solve(first_number, second_number, operator):
    """ 
    solve an operation
    do the given operation to the given numbers

    :param first_number: the first number to the operation on
    :param second_number: the second number to the operation on
    :param operator: the operator to apply to the numbers
    :returns: the problem to be solved as string and the answer to the problem as an integer
    """
    problem = f"{first_number} {operator} {second_number}"              # formulate the problem as a string text
    if operator == '+': answer = first_number + second_number           # solve the problem according the specified operator
    elif operator == '-': answer = first_number - second_number
    else: answer = first_number * second_number
    return problem, answer

def math_quiz():
    """ 
    a math quiz
    the user get to solve a couple of random problem and gets his score at the end
    """
    score = 0   # the score of the user
    TURNS = 3   # how many problems to solve

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(TURNS):
        # generate random numbers and operator
        first_number = get_random_integer_between(1, 10)
        second_number = get_random_integer_between(1, 5)
        operator = get_random_operator()

        # get the text formulation for the problem and the right answer
        problem, answer = solve(first_number, second_number, operator)
        print(f"\nQuestion: {problem}")

        # keep trying to get user input until he gives a valid integer answer
        while True:
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("invalid input try again!")

        # check if the answer of the user is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    
    # print final score
    print(f"\nGame over! Your score is: {score}/{TURNS}")

if __name__ == "__main__":
    math_quiz()
