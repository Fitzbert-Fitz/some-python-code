import random

randoms = 5
available_questions = {1, 2, 3,  5, 8, 9, 10, 12, 13, 16, 17, 18, 19, 20, 24, 25}
random_numbers = []
X=1

while X <= randoms:
    random_numbers.append(random.choice(list(available_questions)))
    X = X + 1
    available_questions.remove(random_numbers[-1])

print("Please answer following Questions", random_numbers)