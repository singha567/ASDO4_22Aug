# Task 3 : investment
print('Task 3 Investment')

var_invest = float(input('please enter initial investment => '))
var_target = float(input('please enter target => '))
var_int = float(input('please enter interest => '))

var_yrs = 1
var_target_reach = var_invest
var_target_reach = var_invest + ((var_int/100)*var_target_reach)
print(var_target_reach)                                 
while var_target_reach < var_target:
    var_target_reach = var_target_reach + ((var_int/100)*var_target_reach)
    
print('Final Value : ',var_target_reach)

#need correction to stop variable. its doing an extra space