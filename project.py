"""" 
Author: Fernando Mendoza
Date: March 29th, 2023
Class: CSE 111
Professor: Brother Luc Comeau
"""
import math

# Explanation of the program
print()
print('Welcome to the retirememt program!')
print()
print('This program will allows you to calculate')
print('how much money you will need to save for your retirement goal.')
print('The program has a menu with 3 options.')
print('The first option will help you find at what age do you want to get retired,')
print('how long will you live after retirement, how much money will you need,')
print('and how much you should save now to achieve your retirement goal.')
print()
print('The second option will help you understand the power of compound interest.')
print('The first option shows you tha you will need to save a lot of money for retirement.')
print('It is because you are not getting any interest from your money.')
print('Compund interest will help you understand that you can save less money if it is earnig an interest rate.')
print('Compound interest is earnig money from your money and from the interest.')
print()
print('The third option will ask you to exit the program.')
print()

# Create main function
def main():
    try:
        menu()
        option = user_selection()
        if option == 1:
            current_age = int(input('What is your current age?: '))
            retirement_age = int(input('At what age to you plan to get retiret?: '))
            life_expectancy = int(input('What is your life expectancy?:  '))
            savings = int(input('How much savings do you already have?: '))
            pension = int(input('How much money will you need monthly after retirement?: '))
            retirement_calculator(current_age, retirement_age, life_expectancy, savings, pension)
            # print(retirement_calculator(retirement_age, life_expectancy, savings, pension)[1])
            main()

        elif option == 2:
            print('Compund Interest Calculator')
            compound_interest()
            main()
        elif option == 3:
            print('The program is over')
        else:
            print('Please enter a value between 1 and 3')
            main()

    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
                " the line number.")

    except IndexError as index_err:
        print()
        print(type(index_err).__name__, index_err, sep=": ")
        
    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")

# Create menu function
def menu():
    print()
    print('1. New Retirement Calculator')
    print('2. Compund Interest Calculator')
    print('3. Exit')
    print()

# User selection menu.
def user_selection():
   selection = int(input('Select an option from the menu: '))
   print()
   return selection

def get_years(expectancy, retirement_age):
        if type(expectancy) != int or expectancy > 100:
            print("Age out of range")
            return None
        return expectancy - retirement_age


def saving_time(retirement_age, current_age):  
    if type(retirement_age) != int or retirement_age > 100:
        print("Age out of range")
        return None
    time_to_save = retirement_age - current_age
    if time_to_save < 0:
        return None
    return time_to_save
    


# Retirement calculator
def retirement_calculator(current_age, retirement_age, expectancy, savings, pension):
    years = get_years(expectancy, retirement_age)
    time_to_save = saving_time(retirement_age, current_age)
    total = (pension * 12) * years
    print()
    print('Results')
    print()
    print(f'Your current age is {current_age} years old')
    print()
    print(f'You want to get retired at {retirement_age} years')
    print()
    print(f'You will need ${pension:,d} to live monthly after retirement')
    print()
    print(f'Your life expectancy after retirement is {years}')
    print()
    if savings != 0:
        total_minus_savings = total - savings
        monthly = total_minus_savings / (time_to_save * 12)
        print(f'Your retirement goal is: ${total:,d}.')
        print(f'Due your current savings of {savings:,d}, your retirement goal will be ${total_minus_savings:,d}')
        print(f'You are going to have {time_to_save} years to save ${total_minus_savings:,d}')
        print(f'You will need to save ${monthly:,.0f} each month per {time_to_save} years to achieve ${total_minus_savings:,d}')

    elif savings == 0:
        monthly = total / (time_to_save * 12)
        print(f'Your retirement goal is: ${total:,d}.')
        print(f'You are going to have {time_to_save} years to save ${total:,d}')
        print(f'You will need to save ${monthly:,.0f} each month per {time_to_save} years to achieve ${total:,d}')
    
    else:
        print("Please, insert a correct value")
    
# Compound interest calculator
def compound_interest(): 

    NewPrinciple = 0
    principle = int(input('How much money you already have for your retirement?: '))
    addition = int(input('How much money will you add to your retirement account annually?: '))
    rate = float(input('What is the annual interest rate of your retirement account?: ' ))
    time = int(input('How many years will you plan to add that amount of money?: '))
    real_rate = rate * 0.01
    i = 2
    first_time =  principle * ( 1 + real_rate)
    NewPrinciple = (first_time + addition)  * ( 1 + real_rate)
    print()
    print('Total year 1 = $',first_time)
    print()
    print(f'Total year 2 = ${NewPrinciple:.2f}')
    print()
    while i < time:
        NewPrinciple = (NewPrinciple + addition)  * ( 1 + real_rate)
        print()
        print(f"Total year {i+1} = ${NewPrinciple:.2f}")
        print()
            
        i = i + 1

    print(f'At the end of {time} years you are going to have ${NewPrinciple:.2f} for your retirement.')
    print()
    print(f'It means that you are going to have ${NewPrinciple/time/12:.2f} monthly after retirement.')
    print()

# Call the jain to start this program
if __name__ == "__main__":
    main()