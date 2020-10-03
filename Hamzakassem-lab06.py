# Hamza Kassem
# A Coffee File Management Program

import KassemH_coffee_records

ADD_COFFEE_CHOICE = 1
QUIT_CHOICE = 6

def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Enter your choice:'))
        if choice == ADD_COFFEE_CHOICE:
            KassemH_coffee_records.add_coffee()
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')

def display_menu():
    print('HAMZA KASSEM COFFEE MANAGEMENT MENU')
    print('1) Add more Coffee Choices to List')
    print('6) Quit')

main()
            


    

    
