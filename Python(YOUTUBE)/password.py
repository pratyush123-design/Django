import random
import string
def generator_password(length=12):
    generate=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(generate) for _ in range(length))
    return password
print(generator_password())
