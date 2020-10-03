# Homework04B hamza kassem
# Uses a for intVariable in [ ] loop
# Uses a for intVariable in range() loop

sales1 = int(input("Enter today's sales for Store 1: "))
sales2 = int(input("Enter today's sales for Store 2: "))
sales3 = int(input("Enter today's sales for Store 3: "))
sales4 = int(input("Enter today's sales for Store 4: "))
sales5 = int(input("Enter today's sales for Store 5: "))
counter = 0
print('SALES BAR CHART')
print('(Each * = $100)')
for sales in [sales1, sales2, sales3, sales4, sales5]:
        counter += 1
        print('Store ', str(counter),': ', sep='', end='')
        for star in range(1, 1 + sales//100):
            print('*',end='')
        print('')       # Causes an end of line to occur
exit = input('')
