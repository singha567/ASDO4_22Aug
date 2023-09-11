# Task 3 - Calculate exam grades with levels

var_mark = int(input('Please enter the student\'s mark '))
print(var_mark)

if var_mark > 0 and var_mark < 101:
    var_level = int(input('Please input student level '))
    print(var_level)

    if var_level == 1:
        if var_mark < 50:
            print('Fail')
        elif var_mark > 49 and var_mark < 61:
            print('Pass')
        elif var_mark > 60 and var_mark < 71:
            print('Merit')
        else:
            print('Distinction')
    elif var_level == 2:
        if var_mark < 40:
            print('Fail')
        elif var_mark > 39 and var_mark < 51:
            print('Pass')
        elif var_mark > 50 and var_mark < 66:
            print('Merit')
        else:
            print('Distinction')
    else:
        print('Error : Value for level should be either 1 or 2')

else:
    print('Error: marks must be between 1 and 100')

