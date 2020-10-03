#Hamza Kassem

import voter

def main():
    first = input('First name: ')
    last = input('Last Name: ')
    idnum = input('Id Number: ')
    propA = input('Proposition A (y/n): ')
    party = input('Party affiliation? (D, R, or I): ')
    if propA == 'Y' or propA == 'y':
        propA = 'Y'
    else:
        propA = 'N' or propA == 'n'
    if party.upper() == 'I':
        info = voter.Voter(first, last, idnum, propA)
        print('Independent')
        print(info)
    if party.upper() == 'D':
        canB = 'y'
        canC = 'Y'
        canB = input('Vote for Candidate B? (y/n): ')
        canC = input('Vote for Candidate C? (y/n): ')
        while canB.upper() == 'Y' and canC.upper() == 'Y':
            canB = input('Vote for candidate B? (y/n): ')
            canC = input('Vote for Candidate C? (y/n): ')
        info = voter.Voter(first, last, idnum, propA)
        print('Democrat')
        print(info)
        if canB.upper() == 'Y':
            print('Candidate B: Yes')
        elif canC.upper() == 'Y':
            print('Candidate C: Yes')
    if party.upper() == 'R':
        canD = input('Vote for candidate D? (y/n): ')
        info = voter.Voter(first, last, idnum, propA)
        print('Republican')
        print(info)
        if canD.upper() == 'Y':
            print('Candidate D: Yes')
        else:
            print('Candidate: No')

main()
input('')
        
        
                         
