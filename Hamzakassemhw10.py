#Hamza Kassem

import emp

def main():
    print('Hamza Kassem')
    name1 = 'Susan Meyers'
    ID1 = '47899'
    department1 = 'accounting'
    title1 = 'Vice President'
    emp1 = emp.Employee(name1, ID1, department1, title1)
    print(emp1)
    print()

    name2 = 'Mark Jones'
    ID2 = '39119'
    department2 = 'IT'
    title2 = 'Programmer'
    emp2 = emp.Employee(name2, ID2, department2, title2)
    print(emp2)
    print()

    name3 = 'Joy Rogers'
    ID3 = '81774'
    department3 = 'Manufacturing'
    title3 = 'Engineer'
    emp3 = emp.Employee(name3, ID3, department3, title3)
    print(emp3)

main()
print('')
