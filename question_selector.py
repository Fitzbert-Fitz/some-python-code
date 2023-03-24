"""Should return some random questions"""

import random

RANDOMS = 5
AVAILABLE_QUESTIONS = {1, 2, 3,  5, 8, 9, 10, 12, 13, 16, 17, 18, 19, 20, 24, 25}
random_questions = []
X=1

while X <= RANDOMS:
    random_questions.append(random.choice(list(AVAILABLE_QUESTIONS)))
    X = X + 1
    AVAILABLE_QUESTIONS.remove(random_questions[-1])

print("Please answer following Questions", random_questions)
