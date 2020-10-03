
# Hamza Kassem Homework04A
# Uses a While Loop to validate the input data
# Uses another While Loop to check to see if you are done

done = False
while not done:
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    score = int(input('Enter your test score: '))
    while score < 0 or score > 100:
        print('Your score must be >= 0 and <= 100.  Please re-enter your test score: ')
        score = int(input('Enter your test score: '))
    if score >= A_score:
        print('Your grade is A.')
    elif score >= B_score:
        print('Your grade is B.')
    elif score >= C_score:
        print('Your grade is C.')
    elif score >= D_score:
        print('Your grade is D.')
    else:
        print('Your grade is F.')
        another = input('Do you want to enter another quiz score? (y/n): ')
        if another == 'y' or another == 'Y':done = False
        else:
            done = True
