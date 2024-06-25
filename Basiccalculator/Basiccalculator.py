# step 1. define the functions needed i.e add sub,mul,div 
# step 2 print options to the user 
# ask for values 
# call the functions 
# while loop to continue the program until the user wants to exit 

    
def add(a, b):
    answer = a + b
    print(f'{a} + {b} = {answer}')

def sub(a, b):
    answer = a - b
    print(f'{a} - {b} = {answer}')
    
def mult(a, b):
    answer = a * b
    print(f'{a} * {b} = {answer}')
    
def div(a, b):
    if b != 0:
        answer = a / b
        print(f'{a} / {b} = {answer}')
    else:
        print('Error: Division by zero is not allowed.')
while True: # you use while if you want the code not to break after excecution ,make it loop
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice = input('Input your choice: ')

    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        sub(a, b)
    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        mult(a, b)
    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        div(a, b)
    elif choice == 'e' or choice == 'E':
        print('End of program')
        quit()
    else:
     print('Invalid choice')
