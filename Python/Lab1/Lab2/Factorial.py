#Task 2 - Factorial

varint = int(input('Please input an integer => '))
print(varint)

var_factor = varint
cnt = varint - 1
while cnt > 0:
    var_factor = var_factor * cnt
    cnt = cnt - 1

print("Factorial value = ",var_factor)
