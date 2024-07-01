import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 15
PROBLEMS = 10

def generate_problem():
    left_side = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_side = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left_side) + operator + str(right_side)
    answer = eval(expression)
    return expression, answer

wrong=0
input("Press any key to start")
print("-----------------------")

start_time = time.time()

for i in range(PROBLEMS):
    expression, answer = generate_problem()
    while True:
        trial = input("Problem #" + str(i+1) + ": " + expression+" = ")
        if trial == str(answer):
            break
        wrong+=1

end_time = time.time()

time_taken = round(end_time - start_time,2)

print("-----------------------")
print(f"Good job! You took {time_taken} seconds and were incorrect {wrong} time(s)" )