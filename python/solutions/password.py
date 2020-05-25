"""
    Generate (mainly) random passwords.
"""

import random

def random_password(n):
    assert n > 2

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '01234567890'
    etc = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()?'

    return ''.join(random.sample(upper, 1) +
                   random.sample(number, 1) +
                   random.sample(etc, n - 2))

if __name__ == "__main__":
    print(random_password(8))
