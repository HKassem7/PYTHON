# Hamza Kassem
# This program will decide if your number is prime or not.

def main():
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'y':
            print('Hamza Kassems prime number checker.')
            num = int(input('Enter a number [integer]: '))
            while not num >= 2:
                print('The number must be equal to or greater than 2')
                print('Re-enter a valid number')
                num = int(input('enter a number [integer]: '))
            isprime(num)
            keep_going = input('Do you want to test another number? [y/n]: ')
            print()
    
def isprime(nuM):
        isprime = True
        for count in range(2, nuM):
                result = nuM % count 
                if result == 0:
                        isprime = False
                if isprime:
                        print('is prime!')
                else:
                        print('is not prime!')

main()
exit = input('')      
                      
                    
    
        
