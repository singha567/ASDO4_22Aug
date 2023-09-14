#Exception handling

try:
    textfilevar = open('filethatdoesnotexist.txt')
    print('The file exists and opened')
    textfilevar.close()
except:
    print('It failed')
    textfilevar = open('filethatdoesnotexist.txt','w')
    textfilevar.close()
    print('I created a file. Try again')