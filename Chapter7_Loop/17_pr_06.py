'''Q6. Write a program to print the following star pattern'''
n=3
for i in range(3): #it defined rows
    print(" " * (n-i-1),end=" ")
    print("*" * (2*i+1),end=" ")
    print(" " * (n-i-1))
