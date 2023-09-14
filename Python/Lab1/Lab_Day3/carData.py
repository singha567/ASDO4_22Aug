# Chapter 7 File IO

fileobjectvar = open("Python/car.csv","r")

grand_total = 0
yr_sales = 0

companies=[]
sales=[]
carsale=[]

for x in range(0,5):
    line = fileobjectvar.readline()
    data = line.strip().split(',')
#    print(data)
    companies.append(data[0])

    print(len(data))
    yr_sales = 0
    for i in range(1,len(data)):
        sales.append(data[i])
        yr_sales = yr_sales + int(data[i])

    carsale.append(yr_sales)
    grand_total += yr_sales
print('************ Companies ******')
print(companies)


sales = list(map(int,sales))
print(sales)
print('******* Company\'s yearly sale  ******')
for i in carsale:
    print(i)
#print(carsale)
print('grand total of sales =>  ',grand_total)
 