'''Q4. Write a recursive function to calculate the sum of first n natural number'''

def sum(n):
    if n==1 :
        return 1
    else :
        return sum(n-1) +n
    
factorial = sum(6)
print(factorial)


