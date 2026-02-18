import random
choice = ("rock","papre","scissor")

running = True
while running:
    player = None 
    computer = random.choice(choice)
    while player not in choice:
        player = input("please enter your choice: ")
        print(f"computer choice{computer}")
        print(f"player choice{player}")
    #all the condition that I can win
    if player == computer :
        print("it's tie")
    elif player == "rock" and computer == "papre":
        print('I win')
    elif player == "paper" and computer == "rock":
        print('I win')
    elif player == 'scissor' and computer == "papre":
        print("You win")
    else:
        print("You lose")
        break