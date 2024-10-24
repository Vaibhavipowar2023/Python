f= open('sample.txt') #by default the mode is r
data = f.readline() #it read first line of the file
print(data) 

data = f.readline() #it read second line line of the file ... and so on
print(data)
f.close()

#note
'''rb : will open for read in binary mode'''
'''rt: will open for read in  text mode'''