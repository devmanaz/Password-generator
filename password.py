import random
import string
def generate_password(length=12):
    char=string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char)for _ in range(length))
    return password
length = int(input("Enter the length "))
password = generate_password(length)
print("password is "+password)

