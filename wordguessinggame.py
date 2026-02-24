import random
with open('word.txt', 'r') as file:
    word = file.read().splitlines()


#guess word
guess_word = random.choice(word).lower()
print(guess_word)
attempt = 6
while True:
    user_guess = input('guess someword: ')
    if user_guess == guess_word:
        print('you are right!!')
    else :
        print('wrong id')
    