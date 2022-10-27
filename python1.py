import random

user = int(input('from\n: '))
for _ in range(user):
    rand = random.randint(0,user)
    print(rand)
    
choice = ['rock','papper','sissors']
print('make choice: rock,papper,sissors,)
user = input('choice\n:)
answer = random.choices(choice)
if user == answer:
             print('won')
elif user != answer:
             print('lost')
