# Chapter 7 File IO

fileobjectvar = open("Python/car.csv","r")

comp_idx = 0
sales_idx = 0

companies=[]
sales=[]

for x in range(0,5):
    line = fileobjectvar.readline()
    print(line)
    data = line.strip().split(',')
    print(data)
    companies.append(data[0])
    #print(companies)

    print(len(data))
    for i in range(1,len(data)):
        sales.append(data[i])

print('************')
print(companies)
print(sales)
sales = list(map(int,sales))
print(sales)


        
#   
#    companies[comp_idx] = 

#print(type(stringvar1))



#for x in range(0,len(stringvar1),2):
#    print(x)
    #if x.isnumeric():
