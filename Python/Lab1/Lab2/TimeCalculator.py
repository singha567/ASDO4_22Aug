# Task 2 - time Calculator
#vardt1 = str(input('Date 1 in format DD:MM:YY => '))
#vardt2 = str(input('Date 2 in format DD:MM:YY => '))
#print(vardt1,'  ',vardt2)

print('Time Calculator')
print('1- Add 2 times ')
print('2- Find the difference between 2 times ')
print('3- Convert to Hours ')
print('4- Convert to Minutes ')
print('5- Convert Minutes to Time ')
print('6- Convert Hours to Time ')
print('7- Convert Days to Time ')
print('8- Exit')
print('')

var_option = 1
dt3 = []
while var_option in range(1,9):
    var_option = int(input('          Enter an option => '))
    print(var_option)
    if var_option in (1,2):
        vardt1 = input('Enter Date 1 in format DD:HH:MM => ')
        dt1 = vardt1.split(':')
        vardt2 = input('Enter Date 2 in format DD:HH:MM => ')
        dt2 = vardt2.split(':')
        print(vardt1,'  ',vardt2)
        print(dt1)
        print(dt2)
        if var_option == 1:
            dt3 = [dt1[0]+dt2[0], dt1[1]+dt2[1], dt1[2]+dt2[2]]
            print(dt3)
#            for i in range(0,3):
#                dt3[i] = int(dt1[i]) + int(dt2[i])
#            print(dt3)
    elif var_option in (3,4,5):
        vardt1 = str(input('Enter Date in format DD:HH:MM => '))
        dt1 = vardt1.split(':')
        if var_option == 3:
            disp_val = (int(dt1[0])*24)+int(dt1[1])+int(int(dt1[2])/24)
            print(disp_val)
        elif var_option == 4:
            disp_val = (int(dt1[0])*1440 + int(dt1[1]*60) + int(dt1[2]))
            print(disp_val)
    



print('Program ended. Thanks! ')