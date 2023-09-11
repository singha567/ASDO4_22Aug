# selection example

inputvar = int(input('Read a number, not 7'))
if inputvar == 7:
    print("You typed 7!!")
    result = inputvar^2
    print("Result = ",result)
else:
    print("well done")

# mple sequential test using elif
#make sure to have things in correct order
if inputvar < 10:
    print("single digit value")
elif inputvar <100:
    print("a double digit")
elif inputvar < 1000:
    print("a triple digit")
else:
    print("huge")

#nesting if statements
# good to have or compare different variables

