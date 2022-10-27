import random

print('provide amont to place bet')
user1 = int(input('ammount\n: '))

choice = ['rock','papper','sissors']
print('make choice: rock,papper,sissors,')
user = input('choice\n:')
answer = random.choices(choice)
if user == answer:
    print('won')
    bet = user1 * 2
    print(f'+ {bet}')
elif user != answer:
    print('lost')
    bet2 = user1 / 2
    print(f'- {bet2}')
