import random

user = int(input('from\n: '))
for _ in range(user):
    rand = random.randint(0,user)
    print(rand)