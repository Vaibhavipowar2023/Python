'''In order to  write to a file, we first open it in write or append mode 
after which, we use the puthon f.write() method to write to the file'''

f = open('another.txt' , 'w')
f.write("Please write this to the file ")

f = open('another.txt' , 'a') # a mode use to append text in file content
f.write(" I am appending")
f.close()