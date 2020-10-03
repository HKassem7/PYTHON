# Hamza Kassem
# This program displays the mean number of files.

def main():
        total = 0.0
        count = 0
        filename = input('Please Enter the Filename desired: ')
        infile = open(filename, 'r')
        for line in infile:
                    amount = float(line)
                    total += amount
                    count += 1
        infile.close()
        mean = total/count
        print('The Mean Value of the numbers in', filename, 'is', format(mean, ',.2f'))

        exit=input('')
main()
