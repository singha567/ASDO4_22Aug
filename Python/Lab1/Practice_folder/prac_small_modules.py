"""
def new_string(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text[-1:-3]
  return "Is" + text[1:2]

print(new_string("Array"))
print(new_string("IsEmpty")) """

set_var = [1,4,6,7,9,2,4]
print(set_var)

count = 0
chk_no = int(input("number = "))
for no in set_var:
    if no == chk_no:
        count += 1

print('Total = '+str(count))
print('Occurance of {} in the set = {}'.format(chk_no, count))

#n (non-negative integer) copies of the first 2 characters of a given string
def result_str(text,n):
    len_str = 2
    if len(text) < len_str:
        len_str = len(text)
    op_str = ""
    for i in range(n):
        op_str = op_str + text[:len_str]
    return op_str

print("final result = ",result_str("abcde",2))
print("final result = ",result_str('a',4))

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))