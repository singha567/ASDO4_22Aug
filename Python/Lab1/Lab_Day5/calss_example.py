#classes
"""
class Classname:
    attribute = "some data"
    def methodname(input):

        return value
"""

class Dog:  ##consider this as template to blueprint
    breed = "labrador"
    weight = 30
    energy = "Medium"
    def communicate(self): #need a paramater always
        return "woof"


goldie = Dog() #object created from blueprint

print(goldie.breed)
print(goldie.energy)
print(goldie.communicate())

bonnie = Dog() 

bonnie.energy = "High"

print(bonnie.breed)
print(bonnie.energy)
print(bonnie.communicate())



#####*********



        