#Count Vowels

var_string = input('Please enter the string => ')
vowel_cnt = 0
for letter in var_string:
    if letter in ('a','e','i','o','u'):
        vowel_cnt += 1

print('Total number of vowels in string ',var_string,' is ',vowel_cnt)