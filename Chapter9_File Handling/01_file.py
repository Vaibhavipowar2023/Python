#use open function to read the content of a file !

# f= open('sample.txt','r')
f= open('sample.txt') #by default the mode is r
data = f.read()
data = f.read(5)  #readd first 5 character of the file content
print(data) #print its content
f.close() #when you open the file uou need to close the file


