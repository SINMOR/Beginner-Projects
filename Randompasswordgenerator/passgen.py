import string
import random

characters =list(string.ascii_letters + string.digits + '!@#$%^&*')


def passgen():
    pass_length = int(input('How long would you like your password to be? '))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(pass_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = ''.join(password)
    
    print(password)
    

option = input('Do you want to generatea password? (Yes/No)')

if option == 'Yes':
    passgen()
elif option == 'No':
    print('Program ended')
    quit()
else:
    print('Invalid output please input yes or no')
    quit()

    
    
    
    
    
    
    
    
    
    
    


