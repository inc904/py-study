import random
import string


def generate_password(length=32):
    charset = string.ascii_letters + string.digits
    return ''.join(random.choice(charset) for _ in range(length))


password = generate_password()

print(password)
