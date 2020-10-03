# Hamza Kassem
# This program will decide if your number is prime or not

def main():
        keep_going = 'y'
        while keep_going == 'y' or keep_going == 'Y':
                print(' Hamza Kassems prime tester')
                num = int(input('Enter a number [integer]: '))
                while not num >=2:
                        print('The number must be greater than or equal to 2')
                        print('Re-enter a valid number')
                        num = int(input('Enter a number [integer]: '))
                for x in range(2, nunm + 1):
                        if isprime(x):
                                print(x)
                keep_going = input('Do you want to test another number? [y/n]: ')
                print()

def isprime(nuM):
        prime = True
        for count in range(2, nuM):
                if nuM % count == 0:
                        prime = False
        return prime

main()
exit = input(' ')
