'''Function is group statement performing a specific task
A function canbe resused by the programmer in given program any number of

syntax : def function() :
            print(hello)'''

def perc(marks):
    return(sum(marks)/400) *100

marks1 = [45,78,87,77]
percentage = perc(marks1)
print(percentage)