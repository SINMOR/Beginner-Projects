# collect the necessary  inputs: principal ,apr,years
# calculate the monthly payment 
# show to the user 

def main():
    print('This is a monthly payment loan program')
    print('')
    
    principal = float(input("input the loan amount: "))
    apr = float(input('Input the annual interest rates: '))
    years= int(input('Input the amount of years: '))
    
    monthly_interest_rate = apr/1200
    months = years*12
    monthly_payment= principal * monthly_interest_rate/(1-(1 + monthly_interest_rate) ** (months))
    print(f'The monthly payment for this loan is :{monthly_payment}')

main(2)