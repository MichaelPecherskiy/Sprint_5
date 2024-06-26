import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def generate_email():
    username_length = random.randint(5, 10)
    domain_length = random.randint(3, 7)
    tld_length = random.randint(2, 3)

    username = generate_random_string(username_length)
    domain = generate_random_string(domain_length)
    tld = generate_random_string(tld_length)

    email = f"{username}@{domain}.{tld}"
    return email


# Пример использования
for i in range(1):
    print(generate_email())