#
"""
filename = input("Input the Filename: ")
f_extns = filename.split(".")
#print ("The extension of the file is : " + print(f_extns[-1])) #this will error due to concating diff types so go either of below 2 options
print ("The extension of the file is : ",print(f_extns[-1]))
print ("The extension of the file is : " + repr(f_extns[-1]))
"""

#value = input('Please enter some comma separated numbers : ')
value = "23,45,1,2,78,456,0,2,23,5"
print('Value entered = ' + value)
print('value inside the list = ',value.split(","))
list_var = value.split(",")
print(list_var)
tuple_var = tuple(list_var)
print(tuple_var)
print('Sorted list = ', list_var.sort())
print(list_var)
print('Reverse list = ', list_var.reverse())
print(list_var)
print('Sorted tuple = ', tuple_var.count(2))

a = 5
n1 = int(str(a) + str(a))
print(n1+n1)

print(abs.__doc__)
#-------
"""
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
"""

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
print(delta)
