import random

def generat_number():
    left_number = random.randint(1, 10) # Used smaller numbers for testing
    right_number = random.randint(1, 10)
    operator = random.choice(['*', '-', '+'])
    expr = str(left_number) + " " + operator + " " + str(right_number)
    answer = eval(expr)
    return expr, answer 

for i in range(3):
    expr, answer = generat_number()
    
    while True:
        user_guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if user_guess == str(answer):
            break
        wrong += 1