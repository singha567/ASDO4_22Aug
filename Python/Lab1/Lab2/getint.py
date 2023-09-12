#Task 4 Input an integer between two limits
var_min = 1
var_max = 100

var_userval = int(input('Please enter a value : '))
cnt = 1
while var_userval < var_max and var_userval > var_min:
    cnt = cnt + 1
    var_userval = int(input('Please enter a value : '))
    if var_userval < var_max and var_userval > var_min:
        break
    else:
        cnt = cnt + 1
