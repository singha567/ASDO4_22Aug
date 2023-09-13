# function for calculating personal tax in UK. 
# chapter 6 Labs

def getIncometax(inputvar):
    pers_allowance = 11850
    if inputvar < 34501:
        taxcalc = (inputvar - pers_allowance)*0.20
    elif inputvar < 1500001:
        taxcalc = (inputvar - pers_allowance)*0.40
    else:
        taxcalc = (inputvar - pers_allowance)*0.45
    return taxcalc

#main
print('Welcome')
salary = float(input('Please enter your salary => '))
print(salary)

print('Tax calculation on your salary = ',getIncometax(salary))




