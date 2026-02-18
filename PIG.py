#random the number between 1 to 6
import random
def roll_die():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
value = roll_die()
print(value)
#input the number of the players between 2 to 4 and check valid input
while True:
    try:
        players_input = input('enter the number of the player:(2-4) ')
        
        players = int(players_input)
        if 2 <= players <= 4:
                break
        else:
                print('please enter a valid number between 2 and 4.')
    except ValueError:
        print('please rnter oonly the inetrger ')
#mix value to win
max_score = 50
#this one is base on the number of players create a list with 0 score
player_scores = [0 for _ in range(players)]
print(player_scores)
current_score = 0
# if no one reach to the mex value continue the game
while max(player_scores) < max_score:
    #let pleyer take turn
    for player_idx in range(players):
        print(f"player {player_idx + 1} 's turn")
        #should roll or not
        while True:
            should_roll = input('would you likw to roll the die (y): ').lower()
            if should_roll != 'y':
                break
            value = roll_die()
            if value == 1:
                print('you roll a 1 you lose all your points this round')
                current_score = 0
                break
            else:
                current_score += value
                print(f'you roll a {value}')
                print(f'your current score for this round is {current_score}')
                
            player_scores[player_idx] += current_score
            print('your total score is now ' + str(player_scores[player_idx]))
