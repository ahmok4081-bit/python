import random
random = random.randint(1,100)
while True:
    user = int(input("please juess the number: "))
    if random == user:
        print("you are right")
        break
    elif random > user:
        print("try again too low ")
    elif random < user:
        print("too high try again!")
    elif user > 100:
        print("you are out of attempts")
        break
        
    else:
        print('invalid input')

