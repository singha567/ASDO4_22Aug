# Practise maths operators and ifelif

var_int = int(input('Please enter an integer number'))
var_float = float(input('Please enter a float number'))

print(var_int,var_float)

print('Basic Calculator')
print('1. Add         +')
print('2. Subtract    -')
print('3. Mulitply    *')
print('4. Divide      /')
print('5. Power      s')

ops_var = input('Please select operation to perform from +,-,*,/,s  ')
print('You selected : ',ops_var)

if ops_var == '+':
    print('Output is : ', var_int + var_float)
elif ops_var == '-':
    print('Output is : ', var_int - var_float)
elif ops_var == '*':
    print('Output is : ', var_int * var_float)
elif ops_var == '/':
    print('Output is : ', var_int / var_float)
elif ops_var == 's':
    print('Output is : ', var_int ** var_float)
else:
    print('Selection is not from the list. Please correct ')
