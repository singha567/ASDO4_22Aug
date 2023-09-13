#Chapter 05 lab
#Pythons inbuilt function

import statistics


data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

#grades = [1,2,3]
grades = data.split(',')
grades = list(map(int,grades))
print(grades)


print('Minimum value = ',min(grades))
print('Maximum value = ',max(grades))

minvalue = min(grades)
maxvalue = max(grades)
avgvalue = round((sum(grades)/len(grades)),2)
meanval = statistics.mean(grades)
medianval = statistics.median(grades)


print('Average = ',round((sum(grades)/len(grades)),2))

print('Mean value = ',statistics.mean(grades))

print('Median value = ',statistics.median(grades))

print('')
print('')
result_str = "Minimum: {}\nMaximum: {}\nAverage: {}\nMean: {}\nMedian: {}".format(minvalue, maxvalue, avgvalue, meanval, medianval)
print(result_str)


     