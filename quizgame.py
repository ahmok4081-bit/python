
quizgame = input('if you want to play the game type yes or no: ').lower()

if quizgame == 'yes':
    print('welcome to the game')
else:
    print('okay bye')
    quit() 
score = 0
answer = input('what is the capital of france? ').lower()
if answer == 'paris':
    print('correct')
    score += 1
else:
    print('wrong answer')
answer2 = input('what is 2 + 2? ')
if answer2 == '4':
    print('correct')
    score += 1
else:
    print('wrong answer')

print('the total score that you get is', score)
