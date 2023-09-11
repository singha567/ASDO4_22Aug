#Exam grade for a student

var_mark = int(input('Please enter the student\'s mark '))
print(var_mark)

if var_mark > 0 and var_mark < 101:
    if var_mark < 50:
        print('Fail')
    elif var_mark > 49 and var_mark < 61:
        print('Pass')
    elif var_mark > 60 and var_mark < 71:
        print('Merit')
    else:
        print('Distinction')
else:
    print('Error: marks must be between 1 and 100')

