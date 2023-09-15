#


class Student:  
    name = "Student1"
    age = 15

    def avg_score(self, stu_name): 
        marks = []
        sum = 0
        for i in range(0,3):
            value = int(input('please enter marks for subject' + str((i+1))))
            print(value)
            sum += value
##            marks.append(input('please enter marks for subject',i+1))
        print("Average marks value for ", stu_name, " = ",round(sum/3,2))
        #        return marks.sum()

year5 = Student()
year5.age = 11
print(year5.name)
print(year5.age)

year5.avg_score(year5.name)


