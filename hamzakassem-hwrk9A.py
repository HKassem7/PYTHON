import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
SAVE = 4
DELETE = 5
QUIT = 6

def main():
    try:
        input_file = open('emailaddresses.dat', 'rb')
        emailaddresses = pickle.load(input_file)
        input_file.close

    except:
        emailaddresses = {}

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(emailaddresses)
        elif choice == ADD:
            add(emailaddresses)
        elif choice == CHANGE:
            change(emailaddresses)
        elif choice == SAVE:
            save(emailaddresses)
        elif choice == DELETE:
            delete(emailaddresses)

def get_menu_choice():
    print()
    print('hamza kassems Email address directory')
    print('-------------------------------')
    print('1. Look up an email address')
    print('2. Add a new email address')
    print('3. Edit an email address')
    print('4. Save an updated email address')
    print('5. Delete an email address')
    print('6. Quit the program')
    print()
        
    choice = int(input('Enter a valid choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

def look_up(emailaddresses):
    name = input('Enter a name: ')

    print(emailaddresses.get(name, 'Not found.'))

def add(emailaddresses):
    name = input('Enter a name: ')
    address = input('Enter an email address: ')

    if name not in emailaddresses:
        emailaddresses[name] = address
    else:
        print('That entry already exists.')

def change(emailaddresses):
    name = input('Enter a name: ')

    if name in emailaddresses:
        emailaddress = input('Enter the new email address: ')

        emailaddresses[name] = emailaddress
    else:
        print('That email is not found.')

def save(emailaddresses):
    output_file = open('emailaddresses.dat', 'wb')
    pickle.dump(emailaddresses, output_file)
    output_file.close()

def delete(emailaddresses):
    name = input('Enter a name: ')

    if name in emailaddresses:
        del emailaddresses[name]
    else:
        print('That name is not found.')

main()
input('')                              
                     
                     
        
    
            

