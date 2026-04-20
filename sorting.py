import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

r = random_numbers(10)
print(r)