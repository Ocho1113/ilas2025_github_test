import random
answer = random.randint(1, 100)
checkcorrect=0

while checkcorrect==0 :
    guess = int(input('guess='))
    print('Your guess is', guess)
    if guess == answer :
        print('Good guess')
        checkcorrect=1
    elif guess < answer:
        print('Too low')
    else:
        print('Too high')