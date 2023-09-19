"""
class Student: 
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name 
student = Student('V12', 'Frank Gibson', 'V')
print(student.__dict__)"""
#**********************************************************************

# *args (Non-Keyword Arguments)
#**kwargs (Keyword Arguments)

def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
myFun('Hello', 'Welcome', 'to', 'Devops Learning')
#---------------------------------------
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value)) 
# main
myFun(first='Devops', mid='Level4', last='Learning')
#---------------------------------------
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_class']}")

 
student_data(student_id='SV12', student_name='Jean Garner')

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')
#****************************************************************************