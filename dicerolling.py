import random
while True:
    ranone = random.randint(1, 6)
    rantwo = random.randint(1, 6)
    ##print(f"the dice two is {rantwo}")
    print(ranone,rantwo)
    user_input = input("do you want to keep play or no Y/N : ")
    if user_input == "Y":
        print('okay bye')
        break
    elif user_input == "N":
        print('ok continous')
        continue    
    else:
        print("invalid input")