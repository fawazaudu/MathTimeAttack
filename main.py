import random

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 15
PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)