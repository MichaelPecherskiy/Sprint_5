import random

PASSWORD = 10


def generate_password(lenght):
    symbols = '1234567890abcdef'
    return ''.join(random.choices(list(symbols), k=lenght))


def generate_random_password():
    return generate_password(PASSWORD)


for i in range(1):
    print(generate_password(lenght=10))
