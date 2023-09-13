# function for calculating personal tax in UK. 
# chapter 6 Labs

def getIncometax(inputvar):
    pers_allowance = 11850
    if inputvar < pers_allowance:
        taxcalc = 0
    elif inputvar > 11851 and inputvar < 34501:
        taxcalc = (inputvar - pers_allowance)*0.20
    elif inputvar > 34500 and inputvar < 1500001:
        taxcalc = (inputvar - pers_allowance)*0.40
    else:
        taxcalc = (inputvar - pers_allowance)*0.45
    return taxcalc

#main
print('Welcome')
salary = input('Please enter your salary => ')
print(salary)
if salary.isnumeric():
    salary = float(salary)
else:
    salary = input('Please enter your salary in numeric value => ')

print('Tax calculation on your salary = ',getIncometax(float(salary)))




