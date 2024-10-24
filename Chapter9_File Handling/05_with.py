'''The best way to open and close the file automatically is the with statement'''
with open('This.txt','r') as f:
    a = f.read() #dont need to write f.close as it is done automatically
print (a)