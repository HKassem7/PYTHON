#Hamza Kassem

import emp
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employee.dat'

def main():
    emplyees = load_employees()
    choice = 0
    while choice !=QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice -- DELETE:
            delete(employees)
    save_employees(employees)

def get_menu_choice():
    print()
    print('Hamza Kassem')
    print('Emplyees information')
    print('1. Look up an employee')
    print('2. Add an employee')
    print("3. Change an employees info")
    print('4. Delete an employee')
    print('5. Quit and save the program')
    print()
    choice = int(input('Enter a choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    return choice

def  look_up(employees):
    name = input('Enter a name: ')
    print(employees.get(name, 'Name not found'))

def add(emplyees):
    name = input('Name: ')
    ID = input('ID Number: ')
    department = input('department: ')
    title = input('Job Title: ')
    entry = emp.Employee(name, ID, department, title)
    if name not in employees:
        employees[name] = entry
        print('Entry has been added')
    else:
        peint('Name already exists')

def change(employees):
    name = input('Enter name: ')
    if name in employees:
        name = input("Enter the emplpyees new name: ")
        ID = input("Enter the emplyees new ID: ")
        department = input("Enter the employees new department: ")
        title = input("Enter the employees new title: ")
        entry = emp.Emplyee(name, ID, department, title)
        print('Information updated')
    else:
        print('NAme not Found')

def delete(employees):
    name = input('Enter a name: ')
    if name in employees:
        del employees[name]
        print('Emtry deleted')
    else:
        print('Name not found')

def save_employees(employees):
    output_file = open(FILENAME, 'wb')
    pickle.dump(employees, output_file)
    output_file.close()

def load_employees():
    try:
        input_file = open(FILENAME, 'rb')
        employee_dct = pickle.load(input_file)
    except:
        employee_dct = {}
    return employee_dct

main()
input('')
    
        
    
