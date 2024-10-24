'''Q8. Write a function to print multiplication table of a give number'''


def mul_table(num,i) :
    no =  num*i
    return no


num1 = int(input("Enter the number"))

for i in range (1, 11):
    n= mul_table(num1, i )
    print(f"{num1} X {i} = {n}") 