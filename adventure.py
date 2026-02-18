# let user input the name 
name = input('enter your name: ')

# welcome + name 
print('welcome to the adventure game ' + name)
#input left or right
direction = input('it come to an end you can go left or right: ').lower()
#if left another input type about the walk or swim
if direction == 'left':
    action = input('you come to the lake would you like to walk around or swim across: ').lower()
    
#if swim print you have eaten by aligotors
    if action == 'swim':
        print('you have been eteaten by aligators. You lost the game.')

#if you walk you ran for miles and you lost the game
    elif action == 'walk':
        print('you walked for a miles and you got lost. you lost the game.')
    
#no left or right print invalid input
else :
    print('invalid input.)')

#if the answer is right let user input again about the cross the bridge or go back
if direction == 'right':
    decision = input('you  come to the bright would you like to cross the bridge or go back: ').lower()
    
#if you go back you lost the game
    if decision == 'go back':
        print('you went back and lost the game.')
#if you cross the bright you meet the strange would you talk to them or no(yes or no)
    elif decision == 'cross the bright':
        meet = input('you meet the sranger would you like to talk to them or not (yes or no): ').lower()
#if yes they give you a goal and you won
        if meet == 'yes':
            print('the stranger gives you a goal you found the goal you won the game!')
#if no you lost the game
        elif meet == 'no':
            print('you ignored the stranger and got lost. you lost the game.')
