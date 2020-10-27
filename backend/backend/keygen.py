from __future__ import print_function
import random
import sys


def generate_secret_key():
    """
        Pseudo-random django secret key generator, from:
        https://github.com/openwisp/ansible-openwisp2/blob/master/files/generate_django_secret_key.py
    """
    chars = 'abcdefghijklmnopqrstuvwxyz' \
        'ABCDEFGHIJKLMNOPQRSTUVXYZ' \
        '0123456789' \
        '#()^[]-_*%&=+/'
    secret_key = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

    return secret_key


def create_secrets():
    """
        Creates secrets.py script with generated SECRET_KEY.
    """

    KEY = generate_secret_key()
    code = f"generated_secret_key = '{KEY}'"
    with open('secrets.py', 'w') as f:
        f.write(code)

        print('From keygen.py : Django secret key generated successfully.')

create_secrets()