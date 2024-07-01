import random

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 15
PROBLEMS = 10

def generate_problem():
    left_side = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_side = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str (left_side) + operator + str(right_side)
    answer = eval(expression)