'''Q1. Write a program using function to find gretest of three numbers'''

def max(a, b, c) :
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else :
        return c
num = max(3, 4, 5)
print("The maximum value is",num)