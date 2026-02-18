master_password = input("Enter the master password: ")
mode = input('would you like to input a new paassword or check an existing password (view or add)type q to quit: ').lower()
def view():
    with open('paawords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
def add():
    name = input('account name: ')
    password = (input('paaword: '))
    with open('paawords.txt', 'a') as f:
        f.write(name + '|' + str(password) + '\n')
while True:
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid input')  
        
    
    
    
    