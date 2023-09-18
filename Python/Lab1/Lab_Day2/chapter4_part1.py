# chapter 04 Lab
#Part 1 

ages=[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

#Record the length
len_ages = len(ages)
print(len_ages)

# Display ages on each line
for i in ages:
    print(i)

#Add one year to every age
#print(ages)
for idx in range(0,len_ages):
    ages[idx] = ages[idx]+1
print(ages)

print("Task 4")
# ***** check this one ****

#only takes into account those people in the age range of 16-65 (inclusively) Please delete all ages which are outside this range.
print(len_ages)
for idx in range(0,len_ages):
    if ages[idx] < 16 or ages[idx] > 65:
        print(ages[idx])
#       ages.remove(ages[idx])
#        del(ages[idx])
    else:
        continue
print(ages)

# Task 5 : display count of 16 to 25 yrs old
print('Task 5 ===== ')
var_16to25 = 0
for idx in range(0,len_ages):
    if (ages[idx] > 15) and (ages[idx] < 26):
        print(ages[idx])
        var_16to25 = var_16to25 + 1
    else:
        continue
print('Total number of 16 to 25 years old = ', var_16to25)

# Task 6 : sort the list
ages.sort()
print(ages)

# Task 7 : proportion of ages fall between 16 to 25
print('proportion of ages fall between 16 to 25 => ', (var_16to25/len_ages)*100,'%')