'''Recursion is funtion call itself'''

#n!= 1 *2*3*4....*n
#n!=n*(n-1)
#factorial 0 is always 1

# def fact(n):
#     factorial = 1
#     for i in range (n) :
#         factorial = factorial *(i+1)
#     return factorial

# f = fact(4)
# print(f)


def fact(n):
    if n==1 or n==0 :
        return 1
    else :
        return n*fact(n-1)
    
factorial = fact(5)
print(factorial)



